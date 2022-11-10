from fastapi import APIRouter, Depends, Security
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.workout import get_group_workouts, get_specific_group_workout, post_workout, edit_workout, delete_workout
from app.schemas.workout import WorkoutBase, WorkoutAdd, WorkoutEdit, PersonalWorkoutAdd
from app.permissions import is_admin, is_manager, is_trainer, is_client, is_not_client
from app.models import User



router = APIRouter(
    tags=["Workouts"],
    prefix="/workout",
)

# Все групповые тренеровки, доступно всем
@router.get('/group', response_model=list[WorkoutBase])
def get_workout_router(db: Session = Depends(get_db)):
    return get_group_workouts(db = db)

# Конкретная групповая тренеровка, доступно всем
@router.get('/group/{id}', response_model=WorkoutBase)
def get_workout_router(id: int, db: Session = Depends(get_db)):
    return get_specific_group_workout(id = id, db = db)



@router.post('/add', response_model=WorkoutBase)
def post_workout_router(workout: WorkoutAdd, db: Session = Depends(get_db), user: User = Security(is_manager)):
    return post_workout(db = db, workout = workout, user = user)

@router.post('/add/personal', response_model=WorkoutBase)
def post_personal_workout_router(workout: PersonalWorkoutAdd, db: Session = Depends(get_db), user: User = Security(is_trainer)):
    return post_workout(db = db, workout = workout, user = user)

@router.put('/edit/{id}', response_model=WorkoutBase)
def edit_workout_router(id:int, workout: WorkoutEdit, db: Session = Depends(get_db), user: User = Security(is_not_client)):
    return edit_workout(id = id, workout = workout, db = db, user = user)

@router.delete('/delete/{id}', status_code=202)
def delete_workout_router(id:int, db: Session = Depends(get_db), user: User = Security(is_not_client)):
    return delete_workout(id = id, db = db)