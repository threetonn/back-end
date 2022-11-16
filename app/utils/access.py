from app.models import Route
from sqlalchemy.orm import Session


def get_access_db(db: Session):
    """ Возвращает список всех роутеров и доступов """
    routes = db.query(Route).all()
    for i in routes:
        i.access = [j.name for j in i.roles]
    return routes