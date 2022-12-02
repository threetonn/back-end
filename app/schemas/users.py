from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    surname: str
    patronymic: str | None = None
    image: str | None = None
    email: EmailStr
    phone: str


class TrainerBase(UserBase):
    """ Информация о тренере """
    bio: str | None = None
    workout_type: list[str]
    
    class Config:
        orm_mode = True


class Gender(BaseModel):
    """ Информация о гендере """
    ru: str
    en: str


class ClientBase(UserBase):
    """ Информация о клиенте """
    gender: Gender
    
    class Config:
        orm_mode = True

class ManagerBase(UserBase):
    """ Информация о клиенте """
    position: str | None = None
    
    class Config:
        orm_mode = True