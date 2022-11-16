from fastapi import APIRouter, Depends, Security
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.workout import (
    get_group_workouts, get_specific_group_workout, 
    get_specific_personal_workout, get_all_client_workouts, 
    get_personal_client_workouts, get_group_client_workouts, 
    post_workout, edit_workout, delete_workout,
    post_subscribe_client, delete_subscription_client,
    get_trainer_workouts, get_trainer_personal_workouts, get_trainer_group_workouts,
    manager_subscribe_client, manager_unsubscribe_client
)
from app.schemas.workout import WorkoutBase, WorkoutAdd, WorkoutEdit, PersonalWorkoutAdd
from app.permissions import is_admin, is_manager, is_trainer, is_client, is_not_client
from app.models import User

from enum import Enum




router = APIRouter(
    prefix="/workout",
)

class Tags(Enum):
    router = "Workout for "
    all = router + "all"
    client = router + "client"
    all_except_client = router + "all except client"
    trainer = router + "trainer"
    manager = router + "manager"


# Все групповые тренеровки, доступно всем
@router.get('/group', response_model=list[WorkoutBase], tags=[Tags.all])
async def get_workout_router(db: Session = Depends(get_db)):
    return get_group_workouts(db = db)


# Конкретная групповая тренеровка, доступно всем
@router.get('/group/{id}', response_model=WorkoutBase, tags=[Tags.all])
async def get_workout_router(id: int, db: Session = Depends(get_db)):
    return get_specific_group_workout(id = id, db = db)


# Все тренеровки клиента
@router.get('/client/me', response_model=list[WorkoutBase], tags=[Tags.client])
async def get_client_workouts(db: Session = Depends(get_db), user: User = Security(is_client)):
    return get_all_client_workouts(db = db, user = user)


# Все персональные тренеровки клиента
@router.get('/client/me/personal', response_model=list[WorkoutBase], tags=[Tags.client])
async def get_client_personal_workouts(
    db: Session = Depends(get_db), 
    user: User = Security(is_client)
    ):
    return get_personal_client_workouts(db = db, user = user)


# Клиент подписывается на групповую тренеровку
@router.post('/group/{id}/subscribe', response_model=list[WorkoutBase], tags=[Tags.client])
async def post_client_subscribe(
    id: int, 
    db: Session = Depends(get_db), 
    user: User = Security(is_client)
    ):
    return post_subscribe_client(id = id, db = db, user = user)


# Клиент отписывается от групповой тренеровки
@router.delete('/group/{id}/unsubscribe', status_code=202, tags=[Tags.client])
async def post_client_unsubscribe(
    id: int, 
    db: Session = Depends(get_db), 
    user: User = Security(is_client)
    ):
    return delete_subscription_client(id = id, db = db, user = user)


# Все групповые тренеровки клиента
@router.get('/client/me/group', response_model=list[WorkoutBase], tags=[Tags.client])
async def get_client_personal_workouts(
    db: Session = Depends(get_db), 
    user: User = Security(is_client)
    ):
    return get_group_client_workouts(db = db, user = user)


# Конеретная персональная тренеровка клиента
@router.get('/personal/{id}', response_model=WorkoutBase, tags=[Tags.client])
async def get_client_personal_workouts(
    id: int, 
    db: Session = Depends(get_db), 
    user: User = Security(is_client)
    ):
    return get_specific_personal_workout(id = id, db = db, user = user)


# Посмотреть все тренеровки которые ведет тренер
@router.get('/trainer/me', response_model=list[WorkoutBase], tags=[Tags.trainer])
async def get_all_trainer_workouts(
    db: Session = Depends(get_db), 
    user: User = Security(is_trainer)
    ):
    return get_trainer_workouts(db = db, user = user)


# Посмотреть все персональные тренеровки которые ведет тренер
@router.get('/trainer/me/personal', response_model=list[WorkoutBase], tags=[Tags.trainer])
async def get_personal_trainer_workouts(
    db: Session = Depends(get_db), 
    user: User = Security(is_trainer)
    ):
    return get_trainer_personal_workouts(db = db, user = user)


# Посмотреть все групповые тренеровки которые ведет тренер
@router.get('/trainer/me/group', response_model=list[WorkoutBase], tags=[Tags.trainer])
async def get_group_trainer_workouts(
    db: Session = Depends(get_db), 
    user: User = Security(is_trainer)
    ):
    return get_trainer_group_workouts(db = db, user = user)


# Создать новую персональную тренеровку, доступно только тренеру
@router.post('/trainer/personal/add', response_model=WorkoutBase, tags=[Tags.trainer])
async def post_personal_workout_router(
    workout: PersonalWorkoutAdd, 
    db: Session = Depends(get_db), 
    user: User = Security(is_trainer)
    ):
    return post_workout(db = db, workout = workout, user = user)


# Изменить персональную тренеровку, доступно только тренеру к которому она относиться
@router.put('/trainer/{id}/edit', response_model=WorkoutBase, tags=[Tags.trainer])
async def edit_personal_workout_router(
    id:int, 
    workout: WorkoutEdit, 
    db: Session = Depends(get_db), 
    user: User = Security(is_trainer)
    ):
    return edit_workout(id = id, workout = workout, db = db, user = user)


# Удалить персональную тренеровку, доступно только тренеру к которому она относиться
@router.delete('/trainer/{id}/delete', tags=[Tags.trainer])
async def delete_personal_workout_router(
    id:int, 
    db: Session = Depends(get_db), 
    user: User = Security(is_trainer)
    ):
    return delete_workout(id = id, db = db, user = user)


# Создать новую групповую тренеровку, доступно только менеджеру
@router.post('/manager/add', response_model=WorkoutBase, tags=[Tags.manager])
async def post_workout_router(
    workout: WorkoutAdd, 
    db: Session = Depends(get_db), 
    user: User = Security(is_manager)
    ):
    return post_workout(db = db, workout = workout, user = user)


# Изменить групповую тренеровку, доступно только менеджеру
@router.put('/manager/{id}/edit', response_model=WorkoutBase, tags=[Tags.manager])
async def edit_group_workout_router(
    id:int, 
    workout: WorkoutEdit, 
    db: Session = Depends(get_db), 
    user: User = Security(is_manager)
    ):
    return edit_workout(id = id, workout = workout, db = db, user = user)


# Удалить существующую тренеровку, доступно всем зарегистрированным пользователям кроме клиента
@router.delete('/manager/{id}/delete', status_code=202, tags=[Tags.manager])
async def delete_group_workout_router(
    id:int, 
    db: Session = Depends(get_db), 
    user: User = Security(is_manager)
    ):
    return delete_workout(id = id, db = db, user = user)


# Менеджер подписывает клиента/ов на групповую тренеровку
@router.put(
    '/manager/{workout_id}/subscribe/', 
    status_code=201,
    tags=[Tags.manager]
    )
async def subscribe_client_to_workout(
    workout_id: int, 
    client_list_id:list[int], 
    db:Session = Depends(get_db), 
    user: User = Security(is_manager)
):
    return manager_subscribe_client(
        workout_id = workout_id, 
        client_list_id = client_list_id, 
        db = db, 
        user = user
    )


# Менеджер отписывает клиента/ов от групповую тренеровку
@router.delete(
    '/manager/{workout_id}/unsubscribe/', 
    status_code=202,
    tags=[Tags.manager]
)
async def unsubscribe_client_from_workout(
    workout_id: int, 
    client_list_id:list[int], 
    db:Session = Depends(get_db), 
    user: User = Security(is_manager)
):
    return manager_unsubscribe_client(
        workout_id = workout_id, 
        client_list_id = client_list_id, 
        db = db, 
        user = user
    )


# Изменить существующую тренеровку, доступно всем зарегистрированным пользователям кроме клиента
@router.put(
    '/edit/{id}', 
    response_model=WorkoutBase, 
    tags=[Tags.all_except_client]
)
async def edit_workout_router(
    id:int, 
    workout: WorkoutEdit, 
    db: Session = Depends(get_db), 
    user: User = Security(is_not_client)
):
    return edit_workout(id = id, workout = workout, db = db, user = user)


# Удалить существующую тренеровку, доступно всем зарегистрированным пользователям кроме клиента
@router.delete(
    '/delete/{id}', 
    status_code=202, 
    tags=[Tags.all_except_client]
)
async def delete_workout_router(
    id:int, 
    db: Session = Depends(get_db), 
    user: User = Security(is_not_client)
):
    return delete_workout(id = id, db = db)