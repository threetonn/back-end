from app.models import Workouttype
from sqlalchemy.orm import Session
from app.schemas.workout_type import ManageWorkoutType

def get_workout_type(request, db: Session):
    """ Возвращает список всех типов тренировок """
    workouttypes = db.query(Workouttype).all()
    port = "" if not request.url.port else f":{ request.url.port }"
    for i in workouttypes:
        i.image = f"http://{ request.url.hostname }{ port }{ i.image }" if i.image else None
    return workouttypes


def get_workout_type_by_id(db: Session, id: int):
    """ Получение типа тренировки по id """
    return db.query(Workouttype).filter(Workouttype.id == id).first()


def add_workout_type(db: Session, workout_type_data: ManageWorkoutType):
    """" Добавление нового типа тренировок """
    db_workout_type = Workouttype(**workout_type_data.__dict__)
    db.add(db_workout_type)
    db.commit()
    db.refresh(db_workout_type)
    return db_workout_type

def edit_workout_type(id: int, db: Session, edited_workout_type_data: ManageWorkoutType):
    """ Изменение типа тренировки """
    db_workout_type = get_workout_type_by_id(db, id)
    workout_type_data_dict = edited_workout_type_data.dict()
    for i in workout_type_data_dict:
        if workout_type_data_dict[i]:
            setattr(db_workout_type, i, workout_type_data_dict[i])
    db.add(db_workout_type)
    db.commit()
    db.refresh(db_workout_type)
    return db_workout_type

def delete_workout_type(id: int, db: Session):
    """ Удаление типа тренировки """
    db_workout_type = get_workout_type_by_id(db, id)
    db.delete(db_workout_type)
    db.commit()
    return { "response": f"Workout type { id } removed" }