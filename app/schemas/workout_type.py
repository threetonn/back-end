from pydantic import BaseModel


class WorkoutTypeBase(BaseModel):
    """ Информация о типах тренировок """
    id: int
    name: str
    description: str
    image: str | None = None

    class Config:
        orm_mode = True


class ManageWorkoutType(BaseModel):
    """ Добавление типа тренировки """
    name: str | None = None
    description: str | None = None

