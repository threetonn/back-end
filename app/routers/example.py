from fastapi import APIRouter, Security
from app.models import User
from app.utils import auth


router = APIRouter(
    tags=["Example"],
)


@router.post('/foradmin')
def secret_data_for_admin(user: User = Security(auth.is_admin)):
    return user


@router.post('/fortrainer')
def secret_data_for_trainer(user: User = Security(auth.is_trainer)):
    return user


@router.post('/formanager')
def secret_data_for_manager(user: User = Security(auth.is_manager)):
    return user