from fastapi import HTTPException
from app.models import Workout, User, Workouttype, Gym
from app.schemas.workout import WorkoutBase, WorkoutAdd, WorkoutEdit
from sqlalchemy.orm import Session, joinedload


def get_workout_out(db: Session, workout: Workout):
    workout.workout_type = workout.WorkoutType.name
    workout.gym = workout.Gym
    trainer = db.query(User).filter(User.id == workout.Trainer).first()
    trainer.gender = trainer.Gender.name
    workout.trainer = trainer


def get_workout_by_id(id: int, db: Session):
    workout = db.query(Workout).filter(Workout.id == id).first()
    
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    return workout


# Пройтись по полям тренеровки, изменить их и вернуть результат
def edit_workout_conditions(id: int, db: Session, workout: WorkoutEdit):
    db_workout = get_workout_by_id(id, db = db)
    edited_workout = workout.dict()
    
    for i in edited_workout:
        if edited_workout[i]:
            if i == "workout_type":
                workout_type_id = db\
                    .query(Workouttype.id)\
                    .filter(Workouttype.name == edited_workout[i])\
                    .first()[0]
                setattr(db_workout, "WorkoutType_id", workout_type_id)
            if i == "gym":
                gym_id = db.query(Gym.id).filter(Gym.name == edited_workout[i]).first()[0]
                setattr(db_workout, "Gym_id", gym_id)
            if i == "trainer":
                trainer_id = db.query(User.id).filter(User.email == edited_workout[i]).first()[0]
                setattr(db_workout, "Trainer", trainer_id)

            setattr(db_workout, i, edited_workout[i])
    
    return db_workout


# Start of the main functions


# Получить все групповые тренеровки
def get_group_workouts(db: Session):
    workouts = db.query(Workout).join(Workouttype).filter(
        Workout.WorkoutType_id == Workouttype.id
        ).filter(
            Workouttype.name != "personal").all()
    
    for workout in workouts:
        get_workout_out(db, workout)
    if not workouts:
        raise HTTPException(status_code=404)
    
    return workouts


# Получить конкретную групповую тренеровку
def get_specific_group_workout(id: int, db: Session):
    workout = db.query(Workout).filter(Workout.id == id).first()
    
    if not workout:
        raise HTTPException(status_code=404)
    elif workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail='Forbidden')
    workout = get_workout_out(db, workout)
    if not workout:
        raise HTTPException(status_code=404)
    
    return workout


# Получить все тренеровки этого клиента
def get_all_client_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts]
    if not workouts:
        raise HTTPException(status_code=404)
    return workouts


# Вернуть все персональные тренеровки клиента
def get_personal_client_workouts(db: Session, user: User):  
    workouts = [get_workout_out(db, workout) for workout in user.Workouts 
                if workout.WorkoutType.name == "personal"]
    if not workouts:
        raise HTTPException(status_code=404)
    return workouts


# Вернуть конкретную персональную тренеровку клиента
def get_specific_personal_workout(id: int, db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts
                if workout.id == id and workout.WorkoutType.name == "personal"]
    if workouts:
        return workouts[0]
    raise HTTPException(status_code=404)


# Вернуть все групповые тренеровки клиента
def get_group_client_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout) for workout in user.Workouts 
                if workout.WorkoutType.name != "personal"]
    if not workouts:
        raise HTTPException(status_code=404)
    return workouts


# Клиент подписываеся на групповую тренеровку
def post_subscribe_client(id: int, db: Session, user: User):
    workout = get_workout_by_id(id, db)
    user.Workouts.append(workout)
    db.add(user)
    db.commit()
    db.refresh(user)
    return get_group_client_workouts(db, user)

# Клиент отписываеся от групповой тренеровки
def delete_subscription_client(id: int, db: Session, user: User):
    workout = get_workout_by_id(id, db)
    
    if not workout:
        raise HTTPException(status_code=404, detail="Workout doesn't exist")
    if not workout in user.Workouts:
        raise HTTPException(status_code=404, detail="User is not subscribed to this workout")
    
    user.Workouts.remove(workout)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"response": f"Unsubscribed from { workout.name } workout!"}


# Вернуть все тренеровки котоые ведет этот тренер
def get_trainer_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout) 
                for workout 
                in db.query(Workout).filter(Workout.Trainer == user.id).all()]
    if not workouts:
        raise HTTPException(status_code=404)
    return workouts


# Вернуть все персональные тренеровки которые ведер этот тренер
def get_trainer_personal_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout)
                for workout
                in db.query(Workout).filter(Workout.Trainer == user.id).all()
                if workout.WorkoutType.name == "personal"]
    if not workouts:
        raise HTTPException(status_code=404)
    return workouts


# Вернуть все групповые тренеровки которые ведет этот тренер
def get_trainer_group_workouts(db: Session, user: User):
    workouts = [get_workout_out(db, workout)
                for workout
                in db.query(Workout).filter(Workout.Trainer == user.id).all()
                if workout.WorkoutType.name != "personal"]
    if not workouts:
        raise HTTPException(status_code=404)
    return workouts


# Создать перональную или групповую тренеровку, доступно тренеру и менеджеру
# Тренер может только создать персональную тренеровку
# Менеджер может создать только групповую тренеровку
def post_workout(db: Session, workout: WorkoutAdd, user: User):
    user_role = user.Role.name
    if not db.query(Gym.id).filter(Gym.name == workout.gym).first():
        raise HTTPException(status_code=404, detail="Gym not found")
    
    db_workout = Workout(
        name = workout.name,
        start_date = workout.start_date,
        end_date = workout.end_date,
        Gym_id = db.query(Gym.id).filter(Gym.name == workout.gym).first()[0]
    )
    
    if user_role == "manager":
        db_workout.WorkoutType_id = db.query(Workouttype.id).filter(
            Workouttype.name == workout.workout_type).first()[0]
        db_workout.Trainer = db.query(User.id).filter(User.email == workout.trainer).first()[0]
    elif user_role == "trainer":
        db_workout.WorkoutType_id = db.query(Workouttype.id).filter(
            Workouttype.name == "personal").first()[0]
        db_workout.Trainer = user.id
    
    if not db_workout:
        raise HTTPException(status_code=404)
    
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    get_workout_out(db, db_workout)
    return db_workout


# Вывести список всех клиентов подписанных на данную тренеровку, доступно только менеджеру
def get_all_subscribed_clients(id: int, db: Session, user: User):
    
    if not get_workout_by_id(db = db, id = id):
        raise HTTPException(status_code=404, detail="Workout not found")

    clients = get_workout_by_id(db = db, id = id).Clients
    
    if not clients:
        raise HTTPException(status_code=404, detail="Clients not found")
    return clients


# Менеджер подписывает клиента/клиентов к групповой тренеровке
def manager_subscribe_client(
    workout_id: int, 
    client_list_id: list[int], 
    db: Session, 
    user: User
):
    workout = get_workout_by_id(workout_id, db)

    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail="Forbidden, workout is personal")
    
    client_list = [
        db.query(User).filter(User.id == client).first()
        for client in client_list_id
        if client
    ]
    
    for client in client_list:
        client.Workouts.append(workout)
        db.add(client)
        db.commit()
        db.refresh(client)


# Менеджер подписывает клиента/ов от групповой тренеровки
def manager_unsubscribe_client(
    workout_id: int, 
    client_list_id: list[int], 
    db: Session, 
    user: User
):
    workout = get_workout_by_id(workout_id, db)

    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    if workout.WorkoutType.name == "personal":
        raise HTTPException(status_code=403, detail="Forbidden, workout is personal")
    
    client_list = [
        db.query(User).filter(User.id == client).first()
        for client in client_list_id
        if client
    ]
    
    for client in client_list:
        client.Workouts.remove(workout)
        db.add(client)
        db.commit()



# Изменить тренеровку, персональную для тренера или групповую для мереджера, только одно из двух
# Доступно только тренеру и менеджеру
def edit_workout(id: int, db: Session, workout: WorkoutEdit, user: User):
    user_role = user.Role.name
    workoutType = get_workout_by_id(id, db = db).WorkoutType.name
    
    if user_role == "trainer" and workoutType == "personal":
        db_workout = edit_workout_conditions(id, db = db, workout = workout)
    elif user_role == "manager" and workoutType != "personal":
        db_workout = edit_workout_conditions(id, db = db, workout = workout)
    else:
        raise HTTPException(status_code=403, detail='Forbidden, wrong user role or workout type')    
    
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    get_workout_out(db, db_workout)
    return db_workout


# Удалить персональную тренеровку - для тенера ИЛИ удалить групповую тренеровку - для мереджера
# ТОЛЬКО одно из двух
def delete_workout(id: int, db: Session, user: User):
    user_role = user.Role.name
    db_workout = get_workout_by_id(id, db = db)
    workout = get_workout_out(db, db_workout)

    if not db_workout:
        raise HTTPException(status_code=404)
    if not workout.WorkoutType.name != "personal" and workout.Trainer == user.id:
        raise HTTPException(status_code=403, detail="Forbidden, wrong trainer")
    if not workout.WorkoutType.name == "personal" and user_role == "trainer":
        raise HTTPException(
            status_code=403, 
            detail="Forbidden, not trainer or not personal workout"
            )
    if not workout.WorkoutType.name != "personal" and user_role == "manager":
        raise HTTPException(
            status_code=403, 
            detail="Forbidden, user is not a manager or is personal workout"
            )
    
    db.delete(db_workout)
    db.commit()
    return {"response": f"Workout { id } deleted!"}