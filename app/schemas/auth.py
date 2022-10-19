from pydantic import BaseModel, EmailStr, PastDate


class Gender(BaseModel):
    name: str


class UserBase(BaseModel):
    """Стандартная информация о пользователе"""
    name: str
    surname: str
    patronomic: str | None = None
    birthday: PastDate
    email: EmailStr
    phonenumber: str
    Gender_id: int
    


class ClientCreate(UserBase):
    """ Проверка sign-up запроса """
    password: str

class UserOut(UserBase):
    id: int
    Role_id: int

    class Config:
        orm_mode = True



class Login(BaseModel):
    """ Проверка login """
    email: EmailStr
    password: str