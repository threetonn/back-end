from pydantic import BaseModel, FutureDate
from datetime import date


class Subscribe(BaseModel):
    start_date: date
    day_count: int



class SubscriptionBase(BaseModel):
    id: int
    type: str
    title: str
    discount: float
    price: float
    features: list[str]

    class Config:
        orm_mode = True


class UserSubscription(BaseModel):
    date_of_purchase: date
    start_date: date
    end_date: date
    day_count: int
    subscription: SubscriptionBase
    is_acting: bool

    class Config:
        orm_mode = True