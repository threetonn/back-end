from fastapi import APIRouter, Security
from app.models import User
from app.permissions import is_admin, is_manager, is_trainer, is_client


router = APIRouter(
    tags=["Example"],
)


@router.post('/forclient')
def secret_data_for_client(user: User = Security(is_client)):
    return {"result": "Ответ приходит только Клиенту"}


@router.post('/fortrainer')
def secret_data_for_trainer(user: User = Security(is_trainer)):
    return {"result": "Ответ приходит только Тренеру"}


@router.post('/formanager')
def secret_data_for_manager(user: User = Security(is_manager)):
    return {"result": "Ответ приходит только Менеджеру"}


@router.post('/foradmin')
def secret_data_for_admin(user: User = Security(is_admin)):
    return {"result": "Ответ приходит только Администратору"}