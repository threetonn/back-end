from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.gym import GymBase
from app.utils.gym import get_gym


router = APIRouter(
    tags=["Gyms"],
    prefix="/gym",
)


@router.get('', response_model=list[GymBase])
def get_gym_router(db: Session = Depends(get_db)):
    return get_gym(db=db)