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
    manager_subscribe_client, manager_unsubscribe_client,
    get_all_subscribed_clients
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


@router.get('/group', response_model=list[WorkoutBase], tags=[Tags.all])
async def get_workout_router(db: Session = Depends(get_db)):
    """ Получить все групповые тренеровки, доступно всем """
    return get_group_workouts(db=db)


@router.get('/group/{id}', response_model=WorkoutBase, tags=[Tags.all])
async def get_workout_router(id: int, db: Session = Depends(get_db)):
    """ Получить конкретную групповую тренеровку, доступно всем """
    return get_specific_group_workout(id=id, db=db)


@router.get('/client/me', response_model=list[WorkoutBase], tags=[Tags.client])
async def get_client_workouts(db: Session = Depends(get_db), user: User = Security(is_client)):
    """ Получить все тренеровки клиента """
    return get_all_client_workouts(db=db, user=user)


@router.get('/client/me/personal', response_model=list[WorkoutBase], tags=[Tags.client])
async def get_client_personal_workouts(
    db: Session = Depends(get_db),
    user: User = Security(is_client)
):
    """ Получить все персональные тренеровки клиента """
    return get_personal_client_workouts(db=db, user=user)


@router.post('/group/{id}/subscribe', response_model=list[WorkoutBase], tags=[Tags.client])
async def post_client_subscribe(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_client)
):
    """ Клиент подписывается на групповую тренеровку """
    return post_subscribe_client(id=id, db=db, user=user)


@router.delete('/group/{id}/unsubscribe', status_code=202, tags=[Tags.client])
async def post_client_unsubscribe(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_client)
):
    """ Клиент отписывается от групповой тренеровки """
    return delete_subscription_client(id=id, db=db, user=user)


@router.get('/client/me/group', response_model=list[WorkoutBase], tags=[Tags.client])
async def get_client_personal_workouts(
    db: Session = Depends(get_db),
    user: User = Security(is_client)
):
    """ Получить все групповые тренеровки клиента """
    return get_group_client_workouts(db=db, user=user)


@router.get('/personal/{id}', response_model=WorkoutBase, tags=[Tags.client])
async def get_client_personal_workouts(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_client)
):
    """ Получить конеретную персональную тренеровку клиента """
    return get_specific_personal_workout(id=id, db=db, user=user)


@router.get('/trainer/me', response_model=list[WorkoutBase], tags=[Tags.trainer])
async def get_all_trainer_workouts(
    db: Session = Depends(get_db),
    user: User = Security(is_trainer)
):
    """ Посмотреть все тренеровки которые ведет тренер """
    return get_trainer_workouts(db=db, user=user)


@router.get('/trainer/me/personal', response_model=list[WorkoutBase], tags=[Tags.trainer])
async def get_personal_trainer_workouts(
    db: Session = Depends(get_db),
    user: User = Security(is_trainer)
):
    """ Посмотреть все персональные тренеровки которые ведет тренер """
    return get_trainer_personal_workouts(db=db, user=user)


@router.get('/trainer/me/group', response_model=list[WorkoutBase], tags=[Tags.trainer])
async def get_group_trainer_workouts(
    db: Session = Depends(get_db),
    user: User = Security(is_trainer)
):
    """ Посмотреть все групповые тренеровки которые ведет тренер """
    return get_trainer_group_workouts(db=db, user=user)


@router.post('/trainer/personal/add', response_model=WorkoutBase, tags=[Tags.trainer])
async def post_personal_workout_router(
    workout: PersonalWorkoutAdd,
    db: Session = Depends(get_db),
    user: User = Security(is_trainer)
):
    """ Создать новую персональную тренеровку, доступно только тренеру """
    return post_workout(db=db, workout=workout, user=user)


@router.put('/trainer/{id}/edit', response_model=WorkoutBase, tags=[Tags.trainer])
async def edit_personal_workout_router(
    id: int,
    workout: WorkoutEdit,
    db: Session = Depends(get_db),
    user: User = Security(is_trainer)
):
    """ Изменить персональную тренеровку, 
    доступно только тренеру к которому она относиться """
    return edit_workout(id=id, workout=workout, db=db, user=user)


@router.delete('/trainer/{id}/delete', tags=[Tags.trainer])
async def delete_personal_workout_router(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_trainer)
):
    """ Удалить персональную тренеровку, 
    доступно только тренеру к которому она относиться """
    return delete_workout(id=id, db=db, user=user)


@router.get('/manager/{id}', tags=[Tags.manager])
async def get_subscribed_clients(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_manager)
):
    """ Получить список клиентов подписанных на данную групповую тренеровку, 
    доступно только менеджеру """
    return get_all_subscribed_clients(id=id, db=db, user=user)


@router.post('/manager/add', response_model=WorkoutBase, tags=[Tags.manager])
async def post_workout_router(
    workout: WorkoutAdd,
    db: Session = Depends(get_db),
    user: User = Security(is_manager)
):
    """ Создать новую групповую тренеровку, доступно только менеджеру """
    return post_workout(db=db, workout=workout, user=user)


@router.put('/manager/{id}/edit', response_model=WorkoutBase, tags=[Tags.manager])
async def edit_group_workout_router(
    id: int,
    workout: WorkoutEdit,
    db: Session = Depends(get_db),
    user: User = Security(is_manager)
):
    """ Изменить групповую тренеровку, доступно только менеджеру """
    return edit_workout(id=id, workout=workout, db=db, user=user)


@router.delete('/manager/{id}/delete', status_code=202, tags=[Tags.manager])
async def delete_group_workout_router(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_manager)
):
    """ Удалить существующую групповую тренеровку, 
    доступно только менеджеру """
    return delete_workout(id=id, db=db, user=user)


@router.post('/manager/{workout_id}/subscribe/', status_code=201, tags=[Tags.manager])
async def subscribe_client_to_workout(
    workout_id: int,
    client_list_id: list[int],
    db: Session = Depends(get_db),
    user: User = Security(is_manager)
):
    """ Менеджер подписывает одного или
     нескольких клиентов на групповую тренеровку """
    return manager_subscribe_client(
        workout_id=workout_id,
        client_list_id=client_list_id,
        db=db,
        user=user
    )


@router.delete('/manager/{workout_id}/unsubscribe/', status_code=202, tags=[Tags.manager])
async def unsubscribe_client_from_workout(
    workout_id: int,
    client_list_id: list[int],
    db: Session = Depends(get_db),
    user: User = Security(is_manager)
):
    """ Менеджер отписывает одного или
    нескольких клиентов от групповой тренеровки """
    return manager_unsubscribe_client(
        workout_id=workout_id,
        client_list_id=client_list_id,
        db=db,
        user=user
    )


@router.put('/edit/{id}', response_model=WorkoutBase, tags=[Tags.all_except_client])
async def edit_workout_router(
    id: int,
    workout: WorkoutEdit,
    db: Session = Depends(get_db),
    user: User = Security(is_not_client)
):
    """ Изменить существующую тренеровку, 
    доступно всем зарегистрированным пользователям кроме клиента """
    return edit_workout(id=id, workout=workout, db=db, user=user)


@router.delete('/delete/{id}', status_code=202, tags=[Tags.all_except_client])
async def delete_workout_router(
    id: int,
    db: Session = Depends(get_db),
    user: User = Security(is_not_client)
):
    """ Удалить существующую тренеровку, 
    доступно всем зарегистрированным пользователям кроме клиента """
    return delete_workout(id=id, db=db)
