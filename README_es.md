<!--
Este archivo README esta generado automaticamente<https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
No se debe editar a mano.
-->

# Rspamd para Yunohost

[![Nivel de integración](https://apps.yunohost.org/badge/integration/rspamd)](https://ci-apps.yunohost.org/ci/apps/rspamd/)
![Estado funcional](https://apps.yunohost.org/badge/state/rspamd)
![Estado En Mantención](https://apps.yunohost.org/badge/maintained/rspamd)

[![Instalar Rspamd con Yunhost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Leer este README en otros idiomas.](./ALL_README.md)*

> *Este paquete le permite instalarRspamd rapidamente y simplement en un servidor YunoHost.*  
> *Si no tiene YunoHost, visita [the guide](https://yunohost.org/install) para aprender como instalarla.*

## Descripción general

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Versión actual:** 3.11.1~ynh1
## Documentaciones y recursos

- Sitio web oficial: <https://rspamd.com/>
- Documentación administrador oficial: <https://rspamd.com/doc>
- Repositorio del código fuente oficial de la aplicación : <https://github.com/rspamd/rspamd>
- Catálogo YunoHost: <https://apps.yunohost.org/app/rspamd>
- Reportar un error: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Información para desarrolladores

Por favor enviar sus correcciones a la [rama `testing`](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

Para probar la rama `testing`, sigue asÍ:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
o
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Mas informaciones sobre el empaquetado de aplicaciones:** <https://yunohost.org/packaging_apps>
