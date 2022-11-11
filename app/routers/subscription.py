from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.subscription import get_subscriptions_db
from app.schemas.subscription import SubscriptionBase


router = APIRouter(
    tags=["Subscriptions"],
    prefix="/subscriptions",
)


@router.get('', response_model=list[SubscriptionBase])
def get_subscriptions(db: Session = Depends(get_db)):
    return get_subscriptions_db(db=db)