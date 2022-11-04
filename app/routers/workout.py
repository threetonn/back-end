from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.workout import get_workout, post_workout, edit_workout, delete_workout
from app.schemas.workout import WorkoutBase, WorkoutAdd, WorkoutEdit


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

@router.put('edit/{id}', response_model=WorkoutBase)
def edit_workout_router(id:int, workout: WorkoutEdit, db: Session = Depends(get_db)):
    return edit_workout(id = id, workout = workout, db = db)

@router.delete('delete/{id}', status_code=202)
def delete_workout_router(id:int, db: Session = Depends(get_db)):
    return delete_workout(id = id, db = db)