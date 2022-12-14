from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.schemas.gym import GymBase

class TrainerBase(BaseModel):
    name: str
    surname: str
    patronymic: str | None = None
    email: EmailStr
    phone: str
    gender: str
    image: str | None = None

    class Config:
        orm_mode = True


class WorkoutAdd(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    workout_type: str
    gym: str
    trainer: EmailStr

    class Config:
        orm_mode = True

class PersonalWorkoutAdd(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    workout_type: str = "personal"
    gym: str
    client_id: int

class WorkoutEdit(BaseModel):
    name: str | None
    start_date: datetime | None
    end_date: datetime | None
    workout_type: str | None
    gym: str | None
    trainer: EmailStr | None


class WorkoutBase(BaseModel):
    id: int
    name: str
    start_date: datetime
    end_date: datetime
    workout_type: str
    gym: GymBase
    trainer: TrainerBase
    clients: list[int]

    class Config:
        orm_mode = True