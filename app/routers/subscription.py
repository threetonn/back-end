from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.subscription import get_subscriptions_db, get_subscription_db, get_features_db
from app.schemas.subscription import SubscriptionBase


router = APIRouter(
    tags=["Subscriptions"],
    prefix="/subscriptions",
)


@router.get('', response_model=list[SubscriptionBase])
def get_subscriptions(db: Session = Depends(get_db)):
    return get_subscriptions_db(db=db)


@router.get('/features')
def get_features(db: Session = Depends(get_db)):
    return get_features_db(db=db)


@router.get('/{id}', response_model=SubscriptionBase)
def get_subscription(id:int, db: Session = Depends(get_db)):
    return get_subscription_db(db=db, id=id)
