from fastapi import APIRouter, Depends, Security
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.subscription import get_subscriptions_db, get_subscription_db, get_features_db, get_subscribe_user, subscribe_db
from app.schemas.subscription import SubscriptionBase, UserSubscription, Subscribe
from app.permissions import is_client
from app.models import User


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


@router.get('/me', response_model=list[UserSubscription])
def get_subscription(db: Session = Depends(get_db), user: User = Security(is_client)):
    return get_subscribe_user(user=user, db=db)


@router.get('/{id}', response_model=SubscriptionBase)
def get_subscription(id:int, db: Session = Depends(get_db)):
    return get_subscription_db(db=db, id=id)
    

@router.post('/{subscriptions_id}/subscribe', response_model=list[UserSubscription])
def subscribe(data: Subscribe, subscriptions_id: int, db: Session = Depends(get_db), user: User = Security(is_client)):
    return subscribe_db(data=data, user=user, subscriptions_id=subscriptions_id, db=db)

