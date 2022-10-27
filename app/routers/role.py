from fastapi import APIRouter, Depends
from app.utils import role
from app.auth_class import Auth
from app.database import get_db
from sqlalchemy.orm import Session


auth_handler = Auth()
router = APIRouter(
    tags=["Role"],
)


@router.get('/roles')
def roles(db: Session = Depends(get_db)):
    return role.get_roles(db)