from fastapi import APIRouter, Depends, Request
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.users import get_trainers_db, get_clients_db, get_managers_db
from app.schemas.users import TrainerBase, ClientBase, ManagerBase


router = APIRouter(
    tags=["Users"],
    prefix="/users",
)


@router.get('/trainers', response_model=list[TrainerBase])
def get_trainers(request: Request, db: Session = Depends(get_db)):
    return get_trainers_db(db=db, request=request)


@router.get('/managers', response_model=list[ManagerBase])
def get_managers(request: Request, db: Session = Depends(get_db)):
    return get_managers_db(db=db, request=request)


@router.get('/clients', response_model=list[ClientBase])
def get_clients(request: Request, search: str = None, db: Session = Depends(get_db)):
    return get_clients_db(db=db, request=request, search=search)