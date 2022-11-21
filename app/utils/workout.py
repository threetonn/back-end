from fastapi import HTTPException
from app.models import Workout, User, Workouttype, Gym, Usersubscription
from app.schemas.workout import WorkoutBase, WorkoutAdd, WorkoutEdit
from app.utils.subscription import get_subscribe_user
from sqlalchemy.orm import Session, joinedload


def get_workout_out(db: Session, workout: Workout):
    workout.workout_type = workout.WorkoutType.name
    workout.gym = workout.Gym
    trainer = db.query(User).filter(User.id == workout.Trainer).first()
    trainer.gender = trainer.Gender.name
    workout.trainer = trainer
    return workout


def get_workout_by_id(id: int, db: Session):
    """ Вытащить из базы данных тренеровку по id """

    workout = db.query(Workout).filter(Workout.id == id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


def edit_workout_conditions(id: int, db: Session, workout: WorkoutEdit):
    """ Пройтись по полям тренеровки, изменить их и вернуть результат """

    db_workout = get_workout_by_id(id, db = db)
    edited_workout = workout.dict()
    
    for workout in edited_workout:
        if not edited_workout[workout]:
            continue
        if workout == "workout_type":
            workout_type_id = db\
                .query(Workouttype.id)\
                .filter(Workouttype.name == edited_workout[workout])\
                .first()[0]
            setattr(db_workout, "WorkoutType_id", workout_type_id)
        if workout == "gym":
            gym_id = db.query(Gym.id)\
                .filter(Gym.name == edited_workout[workout])\
                .first()[0]
            setattr(db_workout, "Gym_id", gym_id)
        if workout == "trainer":
            trainer_id = db.query(User)\
                .filter(User.email == edited_workout[workout])\
                .first()
            user_role = trainer_id.Role.name
            if user_role != "trainer":
                raise HTTPException(status_code=403, detail="User must be a trainer")
            setattr(db_workout, "Trainer", trainer_id.id)
        setattr(db_workout, workout, edited_workout[workout])
    
    return db_workout


def check_subscription(db, user, workout):
    """ Проверить что подписка активна и в ней есть соотвествующий тип тренеровки"""

    client_subscription = get_subscribe_user(db = db, user = user)
    for subscription in client_subscription:
        if subscription.is_acting is not True:
            raise HTTPException(
                status_code=403, 
                detail="Forbidden, subscription is not active!"
            )
        subscription_workouttypes = subscription.Subscription.WorkoutTypes
        for workouttype in subscription_workouttypes:
            if workouttype.id != workout.WorkoutType.id:
                raise HTTPException(
                    status_code=403, 
                    detail="Forbidden, subscription doesn't allow this workout type"
                )
    return True


# Start of the main functions


def get_group_workouts(db: Session):
    """ Получить все групповые тренеровки """

    workouts = db.query(Workout)\
            .join(Workouttype)\
            .filter(Workout.WorkoutType_id == Workouttype.id)\
            .filter(Workouttype.name != "personal").all()
    
    [get_workout_out(db, workout) for workout in workouts]
    if not workouts:
        raise HTTPException(status_code=404, detail="Workouts not found")
    
    return workouts


def get_specific_group_workout(id: int, db: Session):
    """ Получить конкретную групповую тренеровку """

    workout = db.query(Workout).filter(Workout.id == id).first()
    
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail='Forbidden, workout is personal')
    return get_workout_out(db, workout)


def get_all_client_workouts(db: Session, user: User):
    """ Получить все тренеровки этого клиента """

    workouts = [get_workout_out(db, workout) for workout in user.Workouts]
    if not workouts:
        raise HTTPException(status_code=404, detail="Client has no workouts")
    return workouts


def get_personal_client_workouts(db: Session, user: User):  
    """ Вернуть все персональные тренеровки клиента """

    workouts = [get_workout_out(db, workout) 
                for workout in user.Workouts 
                if workout.WorkoutType.name == "personal"]
    if not workouts:
        raise HTTPException(status_code=404, detail="User has no personal workouts")
    return workouts


def get_specific_personal_workout(id: int, db: Session, user: User):
    """ Вернуть конкретную персональную тренеровку клиента """

    workouts = [get_workout_out(db, workout) 
                for workout in user.Workouts
                if workout.id == id 
                and workout.WorkoutType.name == "personal"]
    if workouts:
        return workouts[0]
    raise HTTPException(status_code=404, detail="Personal workout not found")


def get_group_client_workouts(db: Session, user: User):
    """ Вернуть все групповые тренеровки клиента """

    workouts = [get_workout_out(db, workout) 
                for workout in user.Workouts 
                if workout.WorkoutType.name != "personal"]
    if not workouts:
        raise HTTPException(status_code=404, detail="Workouts not found")
    return workouts


def post_subscribe_client(id: int, db: Session, user: User):
    """ Клиент подписываеся на групповую тренеровку """

    workout = get_workout_by_id(id, db)

    if not db.query(Usersubscription).filter(Usersubscription.User_id == user.id).all():
        raise HTTPException(status_code=404, detail="Client has not subscriptions")
    if check_subscription(db = db, user = user, workout = workout) is not True:
        raise HTTPException(
            status_code=403, 
            detail="Forbidden, failed subscription check"
            )
    if user.Role.name != "client":
        raise HTTPException(status_code=403, detail="Forbidden, only client can subscribe")
    user.Workouts.append(workout)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"response": f"Subscribed to { workout.name } workout!"}


def delete_subscription_client(id: int, db: Session, user: User):
    """ Клиент отписываеся от групповой тренеровки """

    workout = get_workout_by_id(id, db)
    
    if not workout:
        raise HTTPException(status_code=404, detail="Workout is not found")
    if not workout in user.Workouts:
        raise HTTPException(status_code=404, detail="User is not subscribed to this workout")
    
    user.Workouts.remove(workout)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"response": f"Unsubscribed from { workout.name } workout!"}


def get_trainer_workouts(db: Session, user: User):
    """ Вернуть все тренеровки которые ведет этот тренер """

    workouts = [get_workout_out(db, workout) 
                for workout 
                in db.query(Workout).filter(Workout.Trainer == user.id).all()]
    if not workouts:
        raise HTTPException(status_code=404, detail="Trainer has no workouts")
    return workouts


def get_trainer_personal_workouts(db: Session, user: User):
    """ Вернуть все персональные тренеровки которые ведер этот тренер """

    workouts = [get_workout_out(db, workout)
                for workout
                in db.query(Workout).filter(Workout.Trainer == user.id).all()
                if workout.WorkoutType.name == "personal"]
    if not workouts:
        raise HTTPException(status_code=404, detail="Trainer has no personal workouts")
    return workouts


def get_trainer_group_workouts(db: Session, user: User):
    """ Вернуть все групповые тренеровки которые ведет этот тренер """

    workouts = [get_workout_out(db, workout)
                for workout
                in db.query(Workout).filter(Workout.Trainer == user.id).all()
                if workout.WorkoutType.name != "personal"]
    if not workouts:
        raise HTTPException(status_code=404, detail="Trainer has no group workouts")
    return workouts


def post_workout(db: Session, workout: WorkoutAdd, user: User):
    """ Создать перональную или групповую тренеровку, доступно тренеру и менеджеру
        Тренер может только создать персональную тренеровку
        Менеджер может создать только групповую тренеровку """

    user_role = user.Role.name
    if not db.query(Gym.id).filter(Gym.name == workout.gym).first():
        raise HTTPException(status_code=404, detail="Gym not found")
    
    db_workout = Workout(
        name = workout.name,
        start_date = workout.start_date,
        end_date = workout.end_date,
        Gym_id = db.query(Gym.id).filter(Gym.name == workout.gym).first()[0]
    )

    if user_role == "manager" and workout.workout_type != "personal":
        db_workout.WorkoutType_id = db.query(Workouttype.id)\
            .filter(Workouttype.name == workout.workout_type)\
            .first()[0]
        db_workout.Trainer = db.query(User.id)\
            .filter(User.email == workout.trainer)\
            .first()[0]
    elif user_role == "trainer" and workout.workout_type == "personal":
        db_workout.WorkoutType_id = db.query(Workouttype.id)\
            .filter(Workouttype.name == "personal")\
            .first()[0]
        db_workout.Trainer = user.id
    else:
        raise HTTPException(status_code=403, detail="Wrong role or workout type")
    
    if not db_workout:
        raise HTTPException(status_code=404)
    
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return get_workout_out(db, db_workout)


def get_all_subscribed_clients(id: int, db: Session, user: User):
    """ Вывести список всех клиентов подписанных на данную тренеровку, 
        доступно только менеджеру """
    
    workout = get_workout_by_id(db = db, id = id)
    if not workout or not workout.Clients:
        raise HTTPException(status_code=404, detail="Workout or clients not found")
    return workout.Clients


def manager_subscribe_client(
    workout_id: int, 
    client_list_id: list[int], 
    db: Session, 
    user: User
):
    """ Менеджер подписывает клиента/клиентов к групповой тренеровке """

    workout = get_workout_by_id(workout_id, db)

    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail="Forbidden, workout is personal")
    if not db.query(Usersubscription).filter(Usersubscription.User_id == user.id).all():
        raise HTTPException(status_code=404, detail="Client has not subscriptions")

    for client in client_list_id:
        client = db.query(User).filter(User.id == client).first()
        if not client:
            continue
        if check_subscription(db = db, user = client, workout = workout) is not True:
            raise HTTPException(
                status_code=403, 
                detail="Forbidden, failed subscription check"
                )
        client.Workouts.append(workout)
        db.add(client)
        db.commit()
        db.refresh(client)
    return {f"Client(s) have been subscribed to { workout.name } workout"}


def manager_unsubscribe_client(
    workout_id: int, 
    client_list_id: list[int], 
    db: Session, 
    user: User
):
    """ Менеджер отписывает клиента/ов от групповой тренеровки """

    workout = get_workout_by_id(workout_id, db)

    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail="Forbidden, workout is personal")
    
    for client in client_list_id:
        client = db.query(User).filter(User.id == client).first()
        if client:
            client.Workouts.remove(workout)
            db.add(client)
            db.commit()
    return {f"Client(s) have been unsubscribed from { workout.name } workout"}


def edit_workout(id: int, db: Session, workout: WorkoutEdit, user: User):
    """ Изменить тренеровку, 
        персональную для тренера или групповую для мереджера, 
        только одно из двух.
        Доступно только тренеру и менеджеру """

    user_role = user.Role.name
    workoutType = get_workout_by_id(id, db = db).WorkoutType.name
    
    if user_role == "trainer" and workoutType == "personal":
        db_workout = edit_workout_conditions(id, db = db, workout = workout)
    elif user_role == "manager" and workoutType != "personal":
        db_workout = edit_workout_conditions(id, db = db, workout = workout)
    else:
        raise HTTPException(
            status_code=403, 
            detail='Forbidden, wrong user role or workout type'
        )
    
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return get_workout_out(db, db_workout)


def delete_workout(id: int, db: Session, user: User):
    """ Удалить персональную тренеровку - для тенера 
        ИЛИ удалить групповую тренеровку - для мереджера
        ТОЛЬКО одно из двух """

    user_role = user.Role.name
    db_workout = get_workout_by_id(id, db = db)
    workout = get_workout_out(db, db_workout)

    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.WorkoutType.name == "personal" and workout.Trainer != user.id:
        raise HTTPException(status_code=403, detail="Forbidden, wrong trainer or workout type")
    if workout.WorkoutType.name != "personal" and user_role != "trainer":
        raise HTTPException(
            status_code=403, 
            detail="Forbidden, not trainer or not personal workout"
            )
    if workout.WorkoutType.name == "personal" and user_role != "manager":
        raise HTTPException(
            status_code=403, 
            detail="Forbidden, user is not a manager or is personal workout"
            )
    
    db.delete(db_workout)
    db.commit()
    return {"response": f"Workout { id } deleted!"}