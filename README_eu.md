<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# Rspamd YunoHost-erako

[![Integrazio maila](https://apps.yunohost.org/badge/integration/rspamd)](https://ci-apps.yunohost.org/ci/apps/rspamd/)
![Funtzionamendu egoera](https://apps.yunohost.org/badge/state/rspamd)
![Mantentze egoera](https://apps.yunohost.org/badge/maintained/rspamd)

[![Instalatu Rspamd YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek Rspamd YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Paketatutako bertsioa:** 3.11.0~ynh1
## Dokumentazioa eta baliabideak

- Aplikazioaren webgune ofiziala: <https://rspamd.com/>
- Administratzaileen dokumentazio ofiziala: <https://rspamd.com/doc>
- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/rspamd/rspamd>
- YunoHost Denda: <https://apps.yunohost.org/app/rspamd>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
edo
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
