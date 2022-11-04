from pydantic import BaseModel, EmailStr, PastDate


class ClientBase(BaseModel):
    """ Информация в профиле клиента """
    name: str
    surname: str
    patronymic: str | None = None
    birthday: PastDate
    email: EmailStr
    phone: str
    gender: str
    image: str | None = None

    class Config:
        orm_mode = True


class WorkoutType(BaseModel):
    """ Информация о типе тренировки """
    id: int
    name: str
    description: str
    image: str | None = None

    class Config:
        orm_mode = True


class TrainerBase(ClientBase):
    """ Информация о профиле тренера """
    bio: str
    workout_type: list[WorkoutType]


class EditUser(BaseModel):
    name: str | None = None
    surname: str | None = None
    patronymic: str | None = None
    phone: str | None = None
    gender: str | None = None
    password: str | None = None

    class Config:
        orm_mode = True


class EditTrainer(EditUser):
    bio: str | None = None
    workout_type: list[int] | None = None