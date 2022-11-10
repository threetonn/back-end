from app.models import Gym
from app.schemas.gym import GymBase
from sqlalchemy.orm import Session


def get_gym(db: Session):
    return db.query(Gym).all()