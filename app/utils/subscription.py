from app.models import Subscription
from sqlalchemy.orm import Session


def get_subscriptions_db(db: Session):
    """ Возвращает список подписок """
    subscriptions = db.query(Subscription).filter(Subscription.is_active == True).all()
    for i in subscriptions:
        i.features = [j.name for j in i.Features] + [j.description for j in i.WorkoutTypes]
        i.price = i.SubscriptionDuration.price
        i.discount = i.SubscriptionDuration.discount
        i.type = i.SubscriptionType.type
        i.title = i.SubscriptionType.name
    return subscriptions

def get_subscription_db(db: Session, id: int):
    """ Возвращает текущую подписку польователя """
    subscription = db.query(Subscription).filter(Subscription.is_active == True).filter(Subscription.id == id).first()
    subscription.features = [j.name for j in subscription.Features] + [j.description for j in subscription.WorkoutTypes]
    subscription.price = subscription.SubscriptionDuration.price
    subscription.discount = subscription.SubscriptionDuration.discount
    subscription.type = subscription.SubscriptionType.type
    subscription.title = subscription.SubscriptionType.name
    return subscription