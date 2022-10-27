from pydantic import BaseModel, EmailStr, PastDate


class RefreshToken(BaseModel):
    """ Получение нового access_token """
    access_token: str


class SignIn(RefreshToken):
    """ Получение access_token и refresh_token """
    refresh_token: str


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