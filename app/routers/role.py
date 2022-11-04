from fastapi import APIRouter, Depends
from app.utils.role import get_roles
from app.auth_class import Auth
from app.database import get_db
from sqlalchemy.orm import Session


auth_handler = Auth()
router = APIRouter(
    tags=["Role"],
)


@router.get('/roles')
def roles(db: Session = Depends(get_db)):
    return get_roles(db)