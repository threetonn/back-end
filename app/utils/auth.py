from app.models import User, Role, Gender
from app.schemas.auth import ClientCreate
from app.auth_class import Auth
from sqlalchemy.orm import Session


auth_handler = Auth()


def get_user_by_email(db: Session, email):
    """ Получение пользователя по email """
    return db.query(User).filter(User.email == email).first()


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