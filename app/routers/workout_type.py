from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.workout_type import get_workout_type
from app.schemas.workout_type import WorkoutTypeBase


router = APIRouter(
    tags=["Workout type"],
    prefix="/workouttype",
)


@router.get('/', response_model=list[WorkoutTypeBase])
def get_workouttype(db: Session = Depends(get_db)):
    return get_workout_type(db=db)