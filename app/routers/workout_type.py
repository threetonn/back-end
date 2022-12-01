from fastapi import APIRouter, Depends, Security, Request
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from app.utils.workout_type import get_workout_type, add_workout_type, edit_workout_type, delete_workout_type
from app.schemas.workout_type import WorkoutTypeBase, ManageWorkoutType
from app.permissions import is_admin


router = APIRouter(
    tags=["Workout type"],
    prefix="/workouttypes",
)


@router.get('', response_model=list[WorkoutTypeBase])
def get_workouttype(request: Request, db: Session = Depends(get_db)):
    return get_workout_type(request=request, db=db)


@router.post('/add', response_model=WorkoutTypeBase)
def add_workouttype(workout_type_data: ManageWorkoutType, db: Session = Depends(get_db), user: User = Security(is_admin)):
    return add_workout_type(db, workout_type_data)


@router.put("/edit/{id}", response_model=WorkoutTypeBase)
def edit_workouttype(id: int, edited_workout_type_data: ManageWorkoutType, db: Session = Depends(get_db), user: User = Security(is_admin)):
    return edit_workout_type(id, db, edited_workout_type_data)


@router.delete('/delete/{id}', status_code=202)
def delete_workouttype(id: int, db: Session = Depends(get_db), user: User = Security(is_admin)):
    return delete_workout_type(id, db)