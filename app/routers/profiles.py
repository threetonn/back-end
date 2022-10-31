from fastapi import APIRouter, Depends, Security
from app.database import get_db
from sqlalchemy.orm import Session
from app.permissions import is_client
from app.models import User
from app.schemas.profiles import ClientBase


router = APIRouter(
    tags=["Profile"],
    prefix="/profile",
)


@router.get('/client')
def profile(db: Session = Depends(get_db), user: User = Security(is_client)):
    return user