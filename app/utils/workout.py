from app.models import Workout, User, Workouttype, Gym
from app.schemas.workout import WorkoutAdd
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