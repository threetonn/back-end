from pydantic import BaseModel, EmailStr, PastDate


class Gender(BaseModel):
    name: str


class UserBase(BaseModel):
    """Стандартная информация о пользователе"""
    name: str
    surname: str
    patronymic: str | None = None
    birthday: PastDate
    email: EmailStr
    phone: str    


class ClientCreate(UserBase):
    """ Проверка sign-up запроса """
    password: str
    gender: str


class UserOut(UserBase):
    id: int
    Role_id: int
    Gender_id: int


    class Config:
        orm_mode = True



class Login(BaseModel):
    """ Проверка login """
    email: EmailStr
    password: str