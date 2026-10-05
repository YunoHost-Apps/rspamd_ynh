#!/usr/bin/env python3
"""
Update Rspamd deb URLs and SHA-256 checksums in manifest.toml.

This script is intended to run from GitHub Actions after a ci-auto-update-*
branch has been created. The version in the manifest is already updated by
the YunoHost updater. The script resolves the matching GitHub tag, obtains
its short commit, and derives the debe URLs from both Debian
sources.
"""

import hashlib
import logging
import os
import re
from pathlib import Path
from typing import Any

import requests
import tomlkit

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.getLogger("urllib3").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

MANIFEST_PATH = Path("manifest.toml")
SOURCES_DEB = ("deb_trixie", "deb_bookworm")
ARCHITECTURES = ("amd64", "arm64")
SHORT_COMMIT_LENGTH = 7


# ========================================================================== #
# Functions customizable by app maintainer


def get_version(manifest: Any) -> str:
    """Return the manifest version before the YunoHost suffix."""
    manifest_version = as_string(manifest["version"])
    version = manifest_version.split("~")[0]
    if not version:
        raise ValueError(
            f"Unable to extract the upstream version from {manifest_version}"
        )

    logger.info("Rspamd version: %s", version)
    return version


def get_github_repository(manifest: Any) -> str:
    """Return the GitHub repository URL from upstream.code."""
    repository = as_string(manifest["upstream"]["code"]).rstrip("/")

    if not re.fullmatch(
        r"https://github\.com/[^/]+/[^/]+",
        repository,
    ):
        raise ValueError(
            f"Unsupported GitHub repository URL: {repository}"
        )

    return repository


def get_tag_commit(
    repository: str,
    version: str,
) -> tuple[str, str]:
    """
    Resolve the commit for the matching GitHub tag or branch.

    The GitHub commits endpoint accepts both tags and branches. The exact
    version is tried first, followed by the same version with a leading 'v'.
    """
    repository_path = repository.removeprefix("https://github.com/")
    api_url = f"https://api.github.com/repos/{repository_path}/commits"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-actions",
    }

    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    for ref in (version, f"v{version}"):
        response = requests.get(
            f"{api_url}/{ref}",
            headers=headers,
            timeout=60,
        )

        if response.status_code == requests.codes.not_found:
            logger.info("GitHub ref not found: %s", ref)
            continue

        response.raise_for_status()
        commit_sha = response.json().get("sha")

        if not commit_sha:
            raise ValueError(
                f"GitHub returned no commit SHA for ref {ref}"
            )

        short_commit = commit_sha[:SHORT_COMMIT_LENGTH]
        logger.info("Resolved ref %s to commit %s", ref, short_commit)
        return ref, short_commit

    raise ValueError(
        f"No GitHub tag or branch found for Rspamd version {version}"
    )


def update_deb_url(
    url: str,
    version: str,
    short_commit: str,
    distribution: str,
) -> str:
    """
    Replace the package version fragment in a Rspamd Debian URL.

    Example:
        4.2.1-1~b7a16ae~trixie
    becomes:
        4.2.1~a1b2c3d~trixie
    """
    replacement = f"{version}~{short_commit}"
    pattern = re.compile(
        rf"(?<=rspamd_)[^/\"']+?"
        rf"(?=~{re.escape(distribution)}_)"
    )

    updated_url, replacements = pattern.subn(
        replacement,
        url,
        count=1,
    )

    if replacements == 1:
        return updated_url

    if f"rspamd_{replacement}~{distribution}_" in url:
        return url

    raise ValueError(
        f"Unable to update {distribution} package version in URL: {url}"
    )


def sha256sum_of_url(url: str) -> str:
    """Compute a remote file checksum without saving the file locally."""
    logger.info("Calculating SHA-256 for %s", url)

    response = requests.get(
        url,
        headers={"User-Agent": "github-actions-rspamd-updater"},
        stream=True,
        timeout=300,
    )
    response.raise_for_status()

    checksum = hashlib.sha256()
    for chunk in response.iter_content(chunk_size=1024 * 1024):
        if chunk:
            checksum.update(chunk)

    return checksum.hexdigest()


# ========================================================================== #
# Core script


def as_string(value: Any) -> str:
    """Return a plain string from a TOMLKit value or a regular string."""
    return value.value if hasattr(value, "value") else str(value)


def main() -> None:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"{MANIFEST_PATH} not found")

    with MANIFEST_PATH.open("r", encoding="utf-8") as manifest_file:
        manifest = tomlkit.load(manifest_file)

    version = get_version(manifest)
    repository = get_github_repository(manifest)
    tag, short_commit = get_tag_commit(repository, version)
    logger.info("Using GitHub ref %s and commit %s", tag, short_commit)

    sources = manifest["resources"]["sources"]

    for source_name in SOURCES_DEB:
        source_deb = sources[source_name]
        logger.info("Updating source %s", source_name)

        for architecture in ARCHITECTURES:
            source = source_deb[architecture]
            current_url = as_string(source["url"])
            updated_url = update_deb_url(
                current_url,
                version,
                short_commit,
                source_name.removeprefix("deb_"),
            )

            if updated_url != current_url:
                logger.info("Updating %s URL", architecture)
                source["url"] = updated_url
            else:
                logger.info("%s URL is already up to date", architecture)

            source["sha256"] = sha256sum_of_url(updated_url)
            logger.info(
                "%s.%s.sha256 = %s",
                source_name,
                architecture,
                as_string(source["sha256"]),
            )

    with MANIFEST_PATH.open("w", encoding="utf-8") as manifest_file:
        tomlkit.dump(manifest, manifest_file)

    logger.info("Updated %s successfully", MANIFEST_PATH)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, requests.RequestException) as exc:
        logger.error("Update failed: %s", exc)
        raise SystemExit(1) from exc
