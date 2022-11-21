from pydantic import BaseModel, EmailStr
from datetime import datetime

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

class GymBase(BaseModel):
    name: str
    address: str

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

class WorkoutEdit(BaseModel):
    name: str | None
    start_date: datetime | None
    end_date: datetime | None
    workout_type: str | None
    gym: str | None
    trainer: EmailStr | None


class WorkoutBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    workout_type: str
    gym: GymBase
    trainer: TrainerBase


    class Config:
        orm_mode = True