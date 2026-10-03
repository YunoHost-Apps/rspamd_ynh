#!/bin/bash

#=================================================
# COMMON VARIABLES AND CUSTOM HELPERS
#=================================================

dkim_whitelist_conf="/etc/rspamd/local.d/whitelist.conf"
dkim_whitelist_marker="Managed by the YunoHost rspamd app"

# Write the DKIM whitelist of the own domains from the comma separated setting
# dkim_whitelist_domains, or remove it when no valid domain is set.
# A whitelist.conf written by hand (without the marker of the template) is left alone.
_add_dkim_whitelist_conf() {
    if [[ -e "$dkim_whitelist_conf" ]] && ! grep -q "$dkim_whitelist_marker" "$dkim_whitelist_conf"; then
        if [[ -n "${dkim_whitelist_domains:-}" ]]; then
            ynh_print_warn "$dkim_whitelist_conf was not written by this app, leaving it alone: the DKIM whitelist setting has no effect until you remove that file."
        fi
        return
    fi

    dkim_whitelist_domains_list=$(echo "${dkim_whitelist_domains:-}" | tr ',' '\n' | sed -e 's/^ *//' -e 's/ *$//' | { grep -E '^[A-Za-z0-9.-]+$' || true; } | sed 's/.*/"&"/' | paste -sd, - | sed 's/,/, /g')
    if [[ -z "$dkim_whitelist_domains_list" ]]; then
        ynh_safe_rm "$dkim_whitelist_conf"
        return
    fi

    ynh_config_add --template="rspamd_whitelist.conf" --destination="$dkim_whitelist_conf"
    chmod 644 "$dkim_whitelist_conf"
}

# Remove the DKIM whitelist, unless it was written by hand
_remove_dkim_whitelist_conf() {
    if grep -qs "$dkim_whitelist_marker" "$dkim_whitelist_conf"; then
        ynh_safe_rm "$dkim_whitelist_conf"
    fi
}
