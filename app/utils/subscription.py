from app.models import Subscription, Feature, Workouttype, Usersubscription, User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime


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
    """ Возвращает конкретную подписку """
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

def get_subscribe_user(user: User, db: Session):
    user_subscriptions = db.query(Usersubscription).filter(Usersubscription.User_id == user.id).all()
    for i in user_subscriptions:
        i.is_acting = False
        if i.start_date <= datetime.now() <= i.end_date:
            i.is_acting = True
    return user_subscriptions
