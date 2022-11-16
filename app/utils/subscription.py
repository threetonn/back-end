from app.models import Subscription, Feature, Workouttype
from sqlalchemy.orm import Session, aliased
from fastapi import HTTPException


def add_a_field(subscription: Subscription):
    subscription.features = [j.name for j in subscription.Features] + [j.description for j in subscription.WorkoutTypes]
    subscription.price = subscription.SubscriptionDuration.price
    subscription.discount = subscription.SubscriptionDuration.discount
    subscription.type = subscription.SubscriptionType.type
    subscription.title = subscription.SubscriptionType.name
    return subscription


def get_subscriptions_db(db: Session):
    """ Возвращает список подписок """
    subscriptions = db.query(Subscription).filter(Subscription.is_active).all()
    for i in subscriptions:
        i = add_a_field(subscription=i)
    return subscriptions

def get_subscription_db(db: Session, id: int):
    """ Возвращает текущую подписку польователя """
    subscription = db.query(Subscription).filter(Subscription.is_active).filter(Subscription.id == id).first()
    if subscription:
        return add_a_field(subscription=subscription)
    raise HTTPException(status_code=404, detail="Subscription is not found")


def get_features_db(db: Session):
    features_db = db.query(Feature.id, Feature.name).all()
    features = [ {"id": i[0], "name": i[1], "type": "features"} for i in features_db ]
    workouttypes_db = db.query(Workouttype.id, Workouttype.description).all()
    workouttypes = [ {"id": i[0], "name": i[1], "type": "workouttypes"} for i in workouttypes_db ]
    return features + workouttypes