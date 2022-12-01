from pydantic import BaseModel

class GymBase(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True