from fastapi import APIRouter, Depends
from app.utils.gender import get_genders
from app.auth_class import Auth
from app.database import get_db
from sqlalchemy.orm import Session


auth_handler = Auth()
router = APIRouter(
    tags=["Gender"],
)


@router.get('/genders')
def genders(db: Session = Depends(get_db)):
    return get_genders(db)