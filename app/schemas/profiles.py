from pydantic import BaseModel, EmailStr, PastDate


class ClientBase(BaseModel):
    """ Информация в профиле клиента """
    name: str
    surname: str
    patronymic: str | None = None
    birthday: PastDate
    email: EmailStr
    phone: str
    image: str | None = None

    class Config:
        orm_mode = True

class TrainerBase(ClientBase):
    """ Информация о профиле тренера """
    bio: str = "О себе"