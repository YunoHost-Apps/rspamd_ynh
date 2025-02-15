<!--
N.B.: This README was automatically generated by <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
It shall NOT be edited by hand.
-->

# Rspamd for YunoHost

[![Integration level](https://apps.yunohost.org/badge/integration/rspamd)](https://ci-apps.yunohost.org/ci/apps/rspamd/)
![Working status](https://apps.yunohost.org/badge/state/rspamd)
![Maintenance status](https://apps.yunohost.org/badge/maintained/rspamd)

[![Install Rspamd with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Read this README in other languages.](./ALL_README.md)*

> *This package allows you to install Rspamd quickly and simply on a YunoHost server.*  
> *If you don't have YunoHost, please consult [the guide](https://yunohost.org/install) to learn how to install it.*

## Overview

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Shipped version:** 3.11.0~ynh1
## Documentation and resources

- Official app website: <https://rspamd.com/>
- Official admin documentation: <https://rspamd.com/doc>
- Upstream app code repository: <https://github.com/rspamd/rspamd>
- YunoHost Store: <https://apps.yunohost.org/app/rspamd>
- Report a bug: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Developer info

Please send your pull request to the [`testing` branch](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

To try the `testing` branch, please proceed like that:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
or
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**More info regarding app packaging:** <https://yunohost.org/packaging_apps>
