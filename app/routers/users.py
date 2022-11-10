from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.users import get_trainers_db
from app.schemas.users import TrainerBase


router = APIRouter(
    tags=["Users"],
    prefix="/users",
)


@router.get('/trainers', response_model=list[TrainerBase])
def get_trainers(db: Session = Depends(get_db)):
    return get_trainers_db(db=db)