from pydantic import BaseModel

class GymBase(BaseModel):
    name: str
    address: str

    class Config:
        orm_mode = True