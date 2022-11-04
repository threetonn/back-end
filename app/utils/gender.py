from app.models import Gender
from sqlalchemy.orm import Session


def get_genders(db: Session):
    """ Возвращает список всех гендеров """
    return db.query(Gender).all()