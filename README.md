Foodgram

Cервис для публикаций и обмена рецептами.

Авторизованные пользователи могут подписываться на понравившихся авторов, добавлять рецепты в избранное, в покупки, скачивать список покупок. Неавторизованным пользователям доступна регистрация, авторизация, просмотр рецептов других пользователей.

Foodgram Workflow

Стек технологий

Python 3.9.7, Django 3.2.7, Django REST Framework 3.12, PostgresQL, Docker, Yandex.Cloud.

Установка

Для запуска локально, создайте файл .env в директории /backend/ с содержанием:

SECRET_KEY=любой_секретный_ключ_на_ваш_выбор
DEBUG=False
ALLOWED_HOSTS=*,или,ваши,хосты,через,запятые,без,пробелов
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=пароль_к_базе_данных_на_ваш_выбор
DB_HOST=bd
DB_PORT=5432
Установка Docker

Для запуска проекта вам потребуется установить Docker и docker-compose.

Для установки на ubuntu выполните следующие команды:

sudo apt install docker docker-compose
Про установку на других операционных системах вы можете прочитать в документации и про установку docker-compose.

Развертывание на локальном сервере

Создайте файл .env Шаблон для заполнения файла нахоится в .env.example.
Выполните команду docker-compose up -d --buld.
Выполните миграции docker-compose exec backend python manage.py migrate.
Создайте суперюзера docker-compose exec backend python manage.py createsuperuser.
Соберите статику docker-compose exec backend python manage.py collectstatic --no-input.
Заполните базу ингредиентами docker-compose exec backend python manage.py import_data.
Документация к API находится по адресу: http://localhost/api/docs/redoc.html.
