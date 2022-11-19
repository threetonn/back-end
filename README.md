## Инициализация проекта

Установка пакета pipenv:

```pip install pipenv```

Установка необходимых пакетов (указанных в Pipfile/Pipfile.lock):

```pipenv install```

Запуск виртуальной среды:

```pipenv shell```

## Инициализация базы данных PostgreSQL

Создание файла db.sql для инициализации БД

```pg_dump -h localhost -p 8005 -U root -F p -f test.sql fitnessclub3tons```

Запуск контейнера базы данных:

```docker compose up -d```

<!-- Подключение к базе данных и настройка:

```docker compose exec db psql fitnessclub3tons --username root --password```

> **Password:** ```root```

> **fitnessclub3tons=#** ```exit``` -->

## Подключение автоматизированной миграции БД

Генерация миграций:

```alembic revision --autogenerate -m "Added required tables"```

Обновление базы данных:

```alembic upgrade head```


## Запуск проекта

```uvicorn app.main:app --reload```


Отключение uvicorn сервера на ubuntu:

```ctrl + \```

## Работа с docker

Остановка базы данных:

```docker compose stop```

Запуск базы данных:

```docker compose start```

Остановка базы данных и удаление контейнера:

``docker compose down``


Команда для создания файла models.py

```sqlacodegen mysql+pymysql://root:admin@127.0.0.1:3306/mydb > app/models.py```