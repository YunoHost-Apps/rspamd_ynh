<!--
Важно: этот README был автоматически сгенерирован <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Он НЕ ДОЛЖЕН редактироваться вручную.
-->

# Rspamd для YunoHost

[![Уровень интеграции](https://apps.yunohost.org/badge/integration/rspamd)](https://ci-apps.yunohost.org/ci/apps/rspamd/)
![Состояние работы](https://apps.yunohost.org/badge/state/rspamd)
![Состояние сопровождения](https://apps.yunohost.org/badge/maintained/rspamd)

[![Установите Rspamd с YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=rspamd)

*[Прочтите этот README на других языках.](./ALL_README.md)*

> *Этот пакет позволяет Вам установить Rspamd быстро и просто на YunoHost-сервер.*  
> *Если у Вас нет YunoHost, пожалуйста, посмотрите [инструкцию](https://yunohost.org/install), чтобы узнать, как установить его.*

## Обзор

Rspamd is an advanced spam filtering system that allows evaluation of messages by a number of rules including regular expressions, statistical analysis and custom services such as URL black lists. Each message is analysed by Rspamd and given a spam score.

According to this spam score and the user’s settings, Rspamd recommends an action for the MTA to apply to the message, for example, to pass, reject or add a header. Rspamd is designed to process hundreds of messages per second simultaneously, and provides a number of useful features.


**Поставляемая версия:** 3.11.0~ynh1
## Документация и ресурсы

- Официальный веб-сайт приложения: <https://rspamd.com/>
- Официальная документация администратора: <https://rspamd.com/doc>
- Репозиторий кода главной ветки приложения: <https://github.com/rspamd/rspamd>
- Магазин YunoHost: <https://apps.yunohost.org/app/rspamd>
- Сообщите об ошибке: <https://github.com/YunoHost-Apps/rspamd_ynh/issues>

## Информация для разработчиков

Пришлите Ваш запрос на слияние в [ветку `testing`](https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing).

Чтобы попробовать ветку `testing`, пожалуйста, сделайте что-то вроде этого:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
или
sudo yunohost app upgrade rspamd -u https://github.com/YunoHost-Apps/rspamd_ynh/tree/testing --debug
```

**Больше информации о пакетировании приложений:** <https://yunohost.org/packaging_apps>
