from app.models import User, Role
from app.auth_class import Auth
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import get_db
from app.utils.auth import get_user_by_email

security = HTTPBearer()
auth_handler = Auth()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """ Получение текущего пользователя """
    token = credentials.credentials
    email = auth_handler.decode_token(token)['sub']
    user =  get_user_by_email(next(get_db()), email)
    if user is None:
        raise HTTPException(status_code=402, detail='Unauthorized')
    return user


def get_role(db: Session, user: User, role: str):
    """ Получение роли пользователя """
    user_role = db.query(Role.name).filter(Role.id == user.Role_id).first()[0]
    if user_role != role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return user


def is_admin(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь администратором """
    return get_role(next(get_db()), user, "Администратор")


def is_manager(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь менеджером """
    return get_role(next(get_db()), user, "Менеджер")


def is_trainer(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь менеджером """
    return get_role(next(get_db()), user, "Тренер")