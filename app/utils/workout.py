from fastapi import HTTPException
from app.models import Workout, User, Workouttype, Gym
from app.schemas.workout import WorkoutAdd, WorkoutEdit
from sqlalchemy.orm import Session

def get_workout_out(db: Session, workout):
    workout.workout_type = workout.WorkoutType.name
    workout.gym = workout.Gym
    trainer = db.query(User).filter(User.id == workout.Trainer).first()
    trainer.gender = trainer.Gender.name
    workout.trainer = trainer

def get_workout(db: Session):
    workouts = db.query(Workout).all()
    for workout in workouts:
        get_workout_out(db, workout)
    
    return workouts


def get_workout_by_id(id: int, db: Session):
    workout = db.query(Workout).filter(Workout.id == id).first()
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


def post_workout(db: Session, workout: WorkoutAdd):
    db_workout = Workout(
        name = workout.name,
        start_date = workout.start_date,
        end_date = workout.end_date,
        WorkoutType_id = db.query(Workouttype.id).filter(Workouttype.name == workout.workout_type).first()[0],
        Gym_id = db.query(Gym.id).filter(Gym.name == workout.gym).first()[0],
        Trainer = db.query(User.id).filter(User.email == workout.trainer).first()[0]
    )
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    get_workout_out(db, db_workout)
    return db_workout


def edit_workout(id: int, db: Session, workout: WorkoutEdit):
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