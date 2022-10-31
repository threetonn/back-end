from pydantic import BaseModel, EmailStr, PastDate


class ClientBase(BaseModel):
    """ Информация в провиле клиента """
    name: str
    surname: str
    patronymic: str | None = None
    birthday: PastDate
    email: EmailStr
    phone: str    