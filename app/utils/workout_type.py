from app.models import Workouttype
from sqlalchemy.orm import Session


def get_workout_type(db: Session):
    """ Возвращает список всех типов тренировок """
    return db.query(Workouttype).all()