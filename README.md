## Инициализация проекта
Установка пакета pipenv:
```pip install pipenv```
Установка необходимых пакетов (указанных в Pipfile/Pipfile.lock):
```pipenv install```
Запуск виртуальной среды:
```pipenv shell```

## Инициализация базы данных PostgreSQL
Запуск контейнера базы данных:
```docker compose up -d```
Подключение к базе данных и настройка:
```docker compose exec db psql fitnessclub3tons --username root --password```
```    Password: root```
```    fitnessclub3tons=# CREATE EXTENSION IF NOT EXISTS "uuid-ossp";```
```    CREATE EXTENSION```
```    fitnessclub3tons=# exit```

## Подключение автоматизированной миграции БД
Генерация миграций:
```alembic revision --autogenerate -m "Added required tables"```
Обновление базы данных:
```alembic upgrade head```

## Запуск проекта
uvicorn app.main:app --reload

## Работа с docker
Остановка базы данных:
```docker compose stop```
Запуск базы данных:
```docker compose start```
Остановка базы данных и удаление контейнера:
``docker compose down``