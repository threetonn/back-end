from app.models import User, Role
from app.schemas.auth import ClientCreate
from app.auth_class import Auth
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import get_db


security = HTTPBearer()
auth_handler = Auth()


def get_user_by_email(db: Session, email):
    """ Получение пользователя по email """
    return db.query(User).filter(User.email == email).first()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """ Получение текущего пользователя """
    token = credentials.credentials
    email = auth_handler.decode_token(token)['sub']
    user =  get_user_by_email(next(get_db()), email)
    if user is None:
        raise HTTPException(status_code=402, detail='Unauthorized')
    return user


def get_role(db: Session, user: User):
    """ Получение роли пользователя """
    role = db.query(Role.name).filter(Role.id == user.Role_id).first()[0]
    return role


def is_admin(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь администратором """
    if get_role(next(get_db())) != "Администратор":
        raise HTTPException(status_code=403, detail='Forbidden')
    return user


def is_manager(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь менеджером """
    if get_role(next(get_db())) != "Менеджер":
        raise HTTPException(status_code=403, detail='Forbidden')
    return user


def is_trainer(user: User = Depends(get_current_user)):
    """ Проверяет является ли пользователь менеджером """
    if get_role(next(get_db())) != "Тренер":
        raise HTTPException(status_code=403, detail='Forbidden')
    return user


def create_user(db: Session, user: ClientCreate):
    """ Создание нового клиента (Role.name = "Клиент") """
    hashed_password = auth_handler.encode_password(user.password)
    db_user = User(
        name = user.name,
        surname = user.surname,
        patronomic = user.patronomic,
        birthday = user.birthday,
        email = user.email,
        phonenumber = user.phonenumber,
        password = hashed_password,
        Gender_id = user.Gender_id,
        Role_id = db.query(Role.id).filter(Role.name == "Клиент").first()[0]
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user