from pydantic import BaseModel


class TrainerBase(BaseModel):
    """ Информация о тренере """
    name: str
    surname: str
    patronymic: str | None = None
    bio: str
    image: str | None = None
    workout_type: list[str]
    
    class Config:
        orm_mode = True