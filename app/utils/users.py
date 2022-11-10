from app.models import User, Role
from sqlalchemy.orm import Session


def get_trainers_db(db: Session):
    """ Возвращает список всех тренеров """
    trainers = db.query(User).join(Role).filter(User.Role_id == Role.id).filter(Role.name == "trainer").all()
    for i in trainers:
        i.workout_type = [i.description for i in i.WorkoutTypes]
    return trainers