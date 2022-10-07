import databases
from os import environ


DB_USER = environ.get("DB_USER")
DB_PASS = environ.get("DB_PASS")
DB_HOST = environ.get("DB_HOST")
DB_NAME = environ.get("DB_NAME")
DB_PORT = environ.get("DB_PORT")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


database = databases.Database(SQLALCHEMY_DATABASE_URL)