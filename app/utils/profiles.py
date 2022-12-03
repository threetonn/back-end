from app.models import User, Workouttype, Usersubscription
from sqlalchemy.orm import Session
from app.schemas.profiles import EditUser, EditTrainer
from app.auth_class import Auth
from app.utils.subscription import get_subscribe_user


auth_handler = Auth()


def get_user_profile(request, user: User, db: Session):
    user.subscription = get_subscribe_user(user=user, db=db)
    port = "" if not request.url.port else f":{ request.url.port }"
    user.image = f"http://{ request.url.hostname }{ port }{ user.image }" if user.image else None
    user.role = user.Role.name
    user.gender = {
        "ru": "Мужчина" if user.Gender.name == "male" else "Женщина",
        "en": user.Gender.name
    }
    return user


def get_trainer_profile(request, user: User):
    port = "" if not request.url.port else f":{ request.url.port }"
    user.image = f"http://{ request.url.hostname }{ port }{ user.image }" if user.image else None
    user.role = user.Role.name
    user.gender = {
        "ru": "Мужчина" if user.Gender.name == "male" else "Женщина",
        "en": user.Gender.name
    }
    user.bio = user.bio if user.bio else "О себе..."
    user.workout_type = user.WorkoutTypes
    for workout_type in user.workout_type:
        workout_type.image = f"http://{ request.url.hostname }{ port }{ workout_type.image }" if workout_type.image else None
    return user


def edit_user_profile(db: Session, user: User, new_data: EditUser):
    modified_user = new_data.dict()
    for i in modified_user:
        if modified_user[i]:
            if i == "password":
                setattr(user, i, auth_handler.encode_password(modified_user[i]))
            elif i == "gender":
                setattr(user, 'Gender_id', 1 if modified_user[i] == 'male' else 2)
            else:
                setattr(user, i, modified_user[i])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def edit_trainer_profile(db: Session, user: User, new_data: EditTrainer):
    modified_user = new_data.dict()
    for i in modified_user:
        if not modified_user[i] is None:
            if i == "password":
                setattr(user, i, auth_handler.encode_password(modified_user[i]))
            elif i == "gender":
                setattr(user, 'Gender_id', 1 if modified_user[i] == 'male' else 2)
            elif i == "workout_type":
                workout_types = db.query(Workouttype).filter(Workouttype.name.in_(modified_user[i])).all()
                user.WorkoutTypes = workout_types
            else:
                setattr(user, i, modified_user[i])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
