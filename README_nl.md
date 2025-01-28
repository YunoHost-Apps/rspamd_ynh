<!--
NB: Deze README is automatisch gegenereerd door <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Hij mag NIET handmatig aangepast worden.
-->

# Rspamd voor Yunohost

[![Integratieniveau](https://apps.yunohost.org/badge/integration/rspamd)](https://ci-apps.yunohost.org/ci/apps/rspamd/)
![Mate van functioneren](https://apps.yunohost.org/badge/state/rspamd)
![Onderhoudsstatus](https://apps.yunohost.org/badge/maintained/rspamd)

[![Rspamd met Yunohost installeren](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Deze README in een andere taal lezen.](./ALL_README.md)*

> *Met dit pakket kun je Rspamd snel en eenvoudig op een YunoHost-server installeren.*  
> *Als je nog geen YunoHost hebt, lees dan [de installatiehandleiding](https://yunohost.org/install), om te zien hoe je 'm installeert.*

## Overzicht

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Geleverde versie:** 3.11.0~ynh1
## Documentatie en bronnen

- Officiele website van de app: <https://rspamd.com/>
- Officiele beheerdersdocumentatie: <https://rspamd.com/doc>
- Upstream app codedepot: <https://github.com/rspamd/rspamd>
- YunoHost-store: <https://apps.yunohost.org/app/rspamd>
- Meld een bug: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Ontwikkelaarsinformatie

Stuur je pull request alsjeblieft naar de [`testing`-branch](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

Om de `testing`-branch uit te proberen, ga als volgt te werk:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
of
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Verdere informatie over app-packaging:** <https://yunohost.org/packaging_apps>
