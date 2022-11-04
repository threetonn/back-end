from app.models import User
from sqlalchemy.orm import Session


def get_trainer_profile(user: User):
    return user