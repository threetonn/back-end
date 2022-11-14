from fastapi import HTTPException
from app.models import Workout, User, Workouttype, Gym
from app.schemas.workout import WorkoutBase, WorkoutAdd, WorkoutEdit
from sqlalchemy.orm import Session


def get_workout_out(db: Session, workout: Workout):
    workout.workout_type = workout.WorkoutType.name
    workout.gym = workout.Gym
    trainer = db.query(User).filter(User.id == workout.Trainer).first()
    trainer.gender = trainer.Gender.name
    workout.trainer = trainer
    return workout


def get_workout_by_id(id: int, db: Session):
    workout = db.query(Workout).filter(Workout.id == id).first()
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


# Start of the main functions


# Получить все групповые тренеровки
def get_group_workouts(db: Session):
    workouts = db.query(Workout).join(Workouttype).filter(Workout.WorkoutType_id == Workouttype.id).filter(Workouttype.name != "personal").all()
    for workout in workouts:
        get_workout_out(db, workout)
    return workouts


# Получить конкретную групповую тренеровку
def get_specific_group_workout(id: int, db: Session):
    workout = db.query(Workout).filter(Workout.id == id).first()
    if not workout:
        raise HTTPException(status_code=404)
    elif workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail='Forbidden')
    workout = get_workout_out(db, workout)
    return workout


# Получить все тренеровки этого клиента
def get_all_client_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts]
    return workouts


# Вернуть все персональные тренеровки клиента
def get_personal_client_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts 
                if workout.WorkoutType.name == "personal"]
    return workouts


# Вернуть конкретную персональную тренеровку клиента
def get_specific_personal_workout(id: int, db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts
                if workout.id == id and workout.WorkoutType.name == "personal"]
    if workouts:
        return workouts[0]
    raise HTTPException(status_code=404)


# Вернуть все групповые тренеровки клиента
def get_group_client_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts 
                if workout.WorkoutType.name != "personal"]
    return workouts


# Клиент подписываеся на групповую тренеровку
def post_subscribe_client(id: int, db: Session, user: User):
    workout = get_workout_by_id(id, db)
    user.Workouts.append(workout)
    db.add(user)
    db.commit()
    db.refresh(user)
    return get_group_client_workouts(db, user)

# Клиент отписываеся от групповой тренеровки
def delete_subscription_client(id: int, db: Session, user: User):
    workout = get_workout_by_id(id, db)
    if not workout:
        raise HTTPException(status_code=404)
    if not workout in user.Workouts:
        raise HTTPException(status_code=404)
    user.Workouts.remove(workout)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"response": f"Unsubscribed from { workout.name } workout!"}


def post_workout(db: Session, workout: WorkoutAdd, user: User):
    user_role = user.Role.name
    db_workout = Workout(
        name = workout.name,
        start_date = workout.start_date,
        end_date = workout.end_date,
        Gym_id = db.query(Gym.id).filter(Gym.name == workout.gym).first()[0]
    )
    if user_role == "manager":
        db_workout.WorkoutType_id = db.query(Workouttype.id).filter(Workouttype.name == workout.workout_type).first()[0]
        db_workout.Trainer = db.query(User.id).filter(User.email == workout.trainer).first()[0]
    elif user_role == "trainer":
        db_workout.WorkoutType_id = db.query(Workouttype.id).filter(Workouttype.name == "personal").first()[0]
        db_workout.Trainer = user.id
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    get_workout_out(db, db_workout)
    return db_workout


def edit_workout_conditions(id: int, db: Session, workout: WorkoutEdit):
    db_workout = get_workout_by_id(id, db = db)
    edited_workout = workout.dict()
    for i in edited_workout:
        if edited_workout[i]:
            if i == "workout_type":
                workout_type_id = db.query(Workouttype.id).filter(Workouttype.name == edited_workout[i]).first()[0]
                setattr(db_workout, "WorkoutType_id", workout_type_id)
            elif i == "gym":
                gym_id = db.query(Gym.id).filter(Gym.name == edited_workout[i]).first()[0]
                setattr(db_workout, "Gym_id", gym_id)
            elif i == "trainer":
                trainer_id = db.query(User.id).filter(User.email == edited_workout[i]).first()[0]
                setattr(db_workout, "Trainer", trainer_id)
            else:
                setattr(db_workout, i, edited_workout[i])
            return db_workout

def edit_workout(id: int, db: Session, workout: WorkoutEdit, user: User):
    user_role = user.Role.name
    workoutType = get_workout_by_id(id, db = db).WorkoutType.name
    if user_role == "trainer" and workoutType == "personal":
        db_workout = edit_workout_conditions(id, db = db, workout = workout)
    elif user_role == "manager" and workoutType != "personal":
        db_workout = edit_workout_conditions(id, db = db, workout = workout)
        print(db_workout)
    else:
        raise HTTPException(status_code=403, detail='Forbidden')

    
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    get_workout_out(db, db_workout)
    return db_workout


def delete_workout(id: int, db: Session):
    db_workout = get_workout_by_id(id, db = db)
    db.delete(db_workout)
    db.commit()
    return {"response": f"Workout { id } deleted!"}