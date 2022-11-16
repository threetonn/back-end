from pydantic import BaseModel

class SubscriptionBase(BaseModel):
    id: int
    type: str
    title: str
    discount: float
    price: float
    features: list[str]

    class Config:
        orm_mode = True