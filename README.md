# Management App
выполнил студент группы ИВТИСмд-11 Черабаев А.А.

## Разворачивание проекта

- установить Docker Desktop и запустить его
- скачать репозиторий: `git clone git@github.com:AndrewCherabaev/management_app.git`
- перейти в папку с поектом: `cd management_app`
- выполнить в консоли `docker-compose up -d`
- создать суперпользователя в интерактивном режиме: `docker-compose exec app python manage.py createsuperuser`
- приложение доступно по адресу `127.0.0.1:8000`