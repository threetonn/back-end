from app.models import Subscription, Feature, Workouttype, Usersubscription, User
from app.schemas.subscription import Subscribe
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta, date


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
        i.subscription = add_a_field(subscription=i.Subscription)
        i.is_acting = True if i.start_date <= datetime.now() <= i.end_date else False
    return user_subscriptions


def check_date_subscribtions(user: User, db: Session, start_date: datetime, day_count: int):
    end_date = start_date + timedelta(day_count)
    if start_date < datetime.now().date() or end_date < datetime.now().date():
        raise HTTPException(status_code=400, detail="Unable to subscribe to past dates")
    user_subscriptions = db\
        .query(Usersubscription)\
        .filter(Usersubscription.User_id == user.id, Usersubscription.end_date >= datetime.now().date())\
        .all()
    for i in user_subscriptions:
        if i.start_date.date() <= start_date <= i.end_date.date() or i.start_date.date() <= end_date <= i.end_date.date():
            raise HTTPException(status_code=400, detail="Subscribed for selected dates already subscribed")
        if start_date <= i.start_date.date() <= end_date or start_date <= i.end_date.date() <= end_date:
            raise HTTPException(status_code=400, detail="Subscribed for selected dates already subscribed")
    return True



def subscribe_db(user: User, data: Subscribe, subscriptions_id:int, db: Session):
    subscriptions = db.query(Subscription).filter(Subscription.id == subscriptions_id).first()
    if not subscriptions:
        raise HTTPException(status_code=404, detail="Subscription is not found")
    if data.day_count > 365:
        raise HTTPException(status_code=400, detail="Subscription is only possible for a year (365 days)")
    if check_date_subscribtions(user=user, db=db, start_date=data.start_date, day_count=data.day_count):
        user_subscription_db = Usersubscription(
            date_of_purchase = datetime.now(),
            start_date = data.start_date,
            end_date = data.start_date + timedelta(data.day_count),
            day_count = data.day_count,
            User_id = user.id,
            Subscription_id = subscriptions_id
        )
        db.add(user_subscription_db)
        db.commit()
        db.refresh(user_subscription_db)
        return get_subscribe_user(user=user, db=db)

