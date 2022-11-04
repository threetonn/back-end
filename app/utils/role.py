from app.models import Role
from sqlalchemy.orm import Session


def get_roles(db: Session):
    """ Возвращает список всех ролей """
    return db.query(Role).all()