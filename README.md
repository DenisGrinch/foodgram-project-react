![example workflow](https://github.com/DenisGrinch/foodgram-project-react/actions/workflows/main.yml/badge.svg)

# Foodgram
### Описание
Foodgram - ресурс на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Foodgram» позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.
### Технологии
- Python 3.7
- Django 2.2.16
- Djangorestframework 3.12.4
- Docker v20.10.17

### Запуск проекта
- Запустите контейнеры командой docker-compose up

- Создайте суперпользователя:
    docker-compose run web python manage.py createsuperuser
- имортируйте данные из дампа:
    docker-compose run web python manage.py loaddata fixtures.json

### Шаблон настройки переменных окружения
- основные параметры для запуска проекта
    - SECRET_KEY=<секретный ключ> 
    - DEBUG=<режим отладки True или False>
    - ALLOWED_HOSTS=<список хостов имеющих доступ к ресурсу>

- параметры для подключения БД

    - ENGINE='django.db.backends.postgresql'
    - NAME='postgres'
    - USER=<имя пользователя БД>
    - PASSWORD=<пароль для подключения к БД>
    - HOST=<имя хоста на котором развёрнута БД>
    - PORT=<порт подключения к БД. поумолчанию '5432'>