from pydantic import BaseModel

class WorkoutTypeBase(BaseModel):
    """ Информация о типах тренировок """
    name: str
    description: str
    image: str | None = None

    class Config:
        orm_mode = True