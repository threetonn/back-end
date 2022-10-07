pipenv shell

docker compose up -d
docker compose exec db psql fitnessclub3tons --username root --password
    Password: root
    fitnessclub3tons=# CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    CREATE EXTENSION
    fitnessclub3tons=# exit

alembic revision --autogenerate -m "Added required tables"
alembic upgrade head
uvicorn app.main:app --reload

docker compose stop
docker compose start

docker compose down