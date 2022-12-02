from app.models import User, Role
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from fastapi import Request


def get_trainers_db(db: Session, request: Request):
    """ Возвращает список всех тренеров """
    trainers = db.query(User).join(Role).filter(User.Role_id == Role.id).filter(Role.name == "trainer").all()
    for i in trainers:
        i.bio = i.bio if i.bio else None
        i.workout_type = [i.description for i in i.WorkoutTypes]
        port = "" if not request.url.port else f":{ request.url.port }"
        i.image = f"http://{ request.url.hostname }{ port }{ i.image }" if i.image else None
    return trainers


def get_managers_db(db: Session, request: Request):
    """ Возвращает список всех менеджеров """
    trainers = db.query(User).join(Role).filter(User.Role_id == Role.id).filter(Role.name == "manager").all()
    for i in trainers:
        i.position = i.bio if i.bio else None
        port = "" if not request.url.port else f":{ request.url.port }"
        i.image = f"http://{ request.url.hostname }{ port }{ i.image }" if i.image else None
    return trainers


def get_clients_db(db: Session, request: Request, search: str):
    """ Возвращает список всех клиентов """
    clients = db.query(User).join(Role).filter(User.Role_id == Role.id, Role.name == "client")
    if search:
        clients = clients.filter(func.concat(User.surname, " ", User.name, " ", User.patronymic).label("full_name").contains(search))
    clients = clients.all()
    for i in clients:
        i.image = f"http://{ request.url.hostname }:{ request.url.port }{ i.image }" if i.image else None
        i.gender = {
            "ru": "Мужчина" if i.Gender.name == "male" else "Женщина",
            "en": i.Gender.name
        }
    return clients