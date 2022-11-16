from pydantic import BaseModel


class RouteBase(BaseModel):
    """ Информация о роуте """
    route: str
    access: list[str]

    class Config:
        orm_mode = True