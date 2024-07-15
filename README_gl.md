<!--
NOTA: Este README foi creado automáticamente por <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON debe editarse manualmente.
-->

# Rspamd para YunoHost

[![Nivel de integración](https://dash.yunohost.org/integration/rspamd.svg)](https://ci-apps.yunohost.org/ci/apps/rspamd/) ![Estado de funcionamento](https://ci-apps.yunohost.org/ci/badges/rspamd.status.svg) ![Estado de mantemento](https://ci-apps.yunohost.org/ci/badges/rspamd.maintain.svg)

[![Instalar Rspamd con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Le este README en outros idiomas.](./ALL_README.md)*

> *Este paquete permíteche instalar Rspamd de xeito rápido e doado nun servidor YunoHost.*  
> *Se non usas YunoHost, le a [documentación](https://yunohost.org/install) para saber como instalalo.*

## Vista xeral

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Versión proporcionada:** 3.9.0~ynh1
## Documentación e recursos

- Web oficial da app: <https://rspamd.com/>
- Documentación oficial para admin: <https://rspamd.com/doc>
- Repositorio de orixe do código: <https://github.com/rspamd/rspamd>
- Tenda YunoHost: <https://apps.yunohost.org/app/rspamd>
- Informar dun problema: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Info de desenvolvemento

Envía a túa colaboración á [rama `testing`](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

Para probar a rama `testing`, procede deste xeito:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
ou
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Máis info sobre o empaquetado da app:** <https://yunohost.org/packaging_apps>
