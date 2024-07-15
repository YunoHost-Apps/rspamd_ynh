<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 Rspamd

[![集成程度](https://dash.yunohost.org/integration/rspamd.svg)](https://ci-apps.yunohost.org/ci/apps/rspamd/) ![工作状态](https://ci-apps.yunohost.org/ci/badges/rspamd.status.svg) ![维护状态](https://ci-apps.yunohost.org/ci/badges/rspamd.maintain.svg)

[![使用 YunoHost 安装 Rspamd](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 Rspamd。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**分发版本：** 3.9.0~ynh1
## 文档与资源

- 官方应用网站： <https://rspamd.com/>
- 官方管理文档： <https://rspamd.com/doc>
- 上游应用代码库： <https://github.com/rspamd/rspamd>
- YunoHost 商店： <https://apps.yunohost.org/app/rspamd>
- 报告 bug： <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
或
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>
