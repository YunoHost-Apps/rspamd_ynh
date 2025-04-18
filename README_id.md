<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# Rspamd untuk YunoHost

[![Tingkat integrasi](https://apps.yunohost.org/badge/integration/rspamd)](https://ci-apps.yunohost.org/ci/apps/rspamd/)
![Status kerja](https://apps.yunohost.org/badge/state/rspamd)
![Status pemeliharaan](https://apps.yunohost.org/badge/maintained/rspamd)

[![Pasang Rspamd dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang Rspamd secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Versi terkirim:** 3.11.1~ynh1
## Dokumentasi dan sumber daya

- Website aplikasi resmi: <https://rspamd.com/>
- Dokumentasi admin resmi: <https://rspamd.com/doc>
- Depot kode aplikasi hulu: <https://github.com/rspamd/rspamd>
- Gudang YunoHost: <https://apps.yunohost.org/app/rspamd>
- Laporkan bug: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
atau
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
