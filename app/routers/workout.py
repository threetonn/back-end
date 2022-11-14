from fastapi import APIRouter, Depends, Security
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.workout import (
    get_group_workouts, get_specific_group_workout, 
    get_specific_personal_workout, get_all_client_workouts, 
    get_personal_client_workouts, get_group_client_workouts, 
    post_workout, edit_workout, delete_workout,
    post_subscribe_client, delete_subscription_client
)
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


# Все тренеровки клиента
@router.get('/client/me', response_model=list[WorkoutBase])
def get_client_workouts(db: Session = Depends(get_db), user: User = Security(is_client)):
    return get_all_client_workouts(db = db, user = user)


# Все персональные тренеровки клиента
@router.get('/client/me/personal', response_model=list[WorkoutBase])
def get_client_personal_workouts(db: Session = Depends(get_db), user: User = Security(is_client)):
    return get_personal_client_workouts(db = db, user = user)


# Клиент подписывается на групповую тренеровку
@router.post('/group/{id}/subscribe', response_model=list[WorkoutBase])
def post_client_subscribe(id: int, db: Session = Depends(get_db), user: User = Security(is_client)):
    return post_subscribe_client(id = id, db = db, user = user)


# Клиент отписывается от групповой тренеровки
@router.delete('/group/{id}/unsubscribe', status_code=202)
def post_client_unsubscribe(id: int, db: Session = Depends(get_db), user: User = Security(is_client)):
    return delete_subscription_client(id = id, db = db, user = user)


# Все групповые тренеровки клиента
@router.get('/client/me/group', response_model=list[WorkoutBase])
def get_client_personal_workouts(db: Session = Depends(get_db), user: User = Security(is_client)):
    return get_group_client_workouts(db = db, user = user)


# Конеретная персональная тренеровка клиента
@router.get('/personal/{id}', response_model=WorkoutBase)
def get_client_personal_workouts(id: int, db: Session = Depends(get_db), user: User = Security(is_client)):
    return get_specific_personal_workout(id = id, db = db, user = user)


# Создать новую групповую тренеровку, доступно только менеджеру
@router.post('/add', response_model=WorkoutBase)
def post_workout_router(workout: WorkoutAdd, db: Session = Depends(get_db), user: User = Security(is_manager)):
    return post_workout(db = db, workout = workout, user = user)


# Создать новую персональную тренеровку, доступно только тренеру
@router.post('/add/personal', response_model=WorkoutBase)
def post_personal_workout_router(workout: PersonalWorkoutAdd, db: Session = Depends(get_db), user: User = Security(is_trainer)):
    return post_workout(db = db, workout = workout, user = user)


# Изменить существующую тренеровку, доступно всем зарегистрированным пользователям кроме клиента
@router.put('/edit/{id}', response_model=WorkoutBase)
def edit_workout_router(id:int, workout: WorkoutEdit, db: Session = Depends(get_db), user: User = Security(is_not_client)):
    return edit_workout(id = id, workout = workout, db = db, user = user)


# Удалить существующую тренеровку, доступно всем зарегистрированным пользователям кроме клиента
@router.delete('/delete/{id}', status_code=202)
def delete_workout_router(id:int, db: Session = Depends(get_db), user: User = Security(is_not_client)):
    return delete_workout(id = id, db = db)