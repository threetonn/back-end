from app.models import User
from app.auth_class import Auth
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import get_db
from app.utils.auth import get_user_by_email

security = HTTPBearer()
auth_handler = Auth()


def get_current_user(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)):
    """ Получение текущего пользователя """
    token = credentials.credentials
    email = auth_handler.decode_token(token)
    user =  get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=402, detail='Unauthorized')
    return user


def get_role(user: User, role: str):
    """ Получение роли пользователя """
    if user.Role.name == role:
        return user
    raise HTTPException(status_code=403, detail='Forbidden, wrong role')


# id | name
# 1  | Клиент
# 2  | Тренер
# 3  | Менеджер
# 4  | Администратор


def is_client(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь клиентом """
    return get_role(user, "client")


def is_trainer(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь менеджером """
    return get_role(user, "trainer")


def is_manager(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь менеджером """
    return get_role(user, "manager")


def is_admin(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь администратором """
    return get_role(user, "admin")


def is_not_client(user: User = Depends(get_current_user)):
    """ Проверяет если пользователь не является клиентом """
    if user.Role.name == "client":
        raise HTTPException(status_code=403, detail='Forbidden, user is a client')
    return user
