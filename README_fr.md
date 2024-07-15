<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Rspamd pour YunoHost

[![Niveau d’intégration](https://dash.yunohost.org/integration/rspamd.svg)](https://ci-apps.yunohost.org/ci/apps/rspamd/) ![Statut du fonctionnement](https://ci-apps.yunohost.org/ci/badges/rspamd.status.svg) ![Statut de maintenance](https://ci-apps.yunohost.org/ci/badges/rspamd.maintain.svg)

[![Installer Rspamd avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Rspamd rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Version incluse :** 3.9.0~ynh1
## Documentations et ressources

- Site officiel de l’app : <https://rspamd.com/>
- Documentation officielle de l’admin : <https://rspamd.com/doc>
- Dépôt de code officiel de l’app : <https://github.com/rspamd/rspamd>
- YunoHost Store : <https://apps.yunohost.org/app/rspamd>
- Signaler un bug : <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
ou
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
