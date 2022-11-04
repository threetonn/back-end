from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.workout import get_workout, post_workout
from app.schemas.workout import WorkoutBase, WorkoutAdd


router = APIRouter(
    tags=["Workouts"],
    prefix="/workout",
)


@router.get('', response_model=list[WorkoutBase])
def get_workout_router(db: Session = Depends(get_db)):
    return get_workout(db=db)


@router.post('add', response_model=WorkoutBase)
def post_workout_router(workout: WorkoutAdd, db: Session = Depends(get_db)):
    return post_workout(db = db, workout = workout)