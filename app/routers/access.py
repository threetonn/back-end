from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.access import get_access_db
from app.schemas.access import RouteBase


router = APIRouter(
    tags=["Access to router"],
)


# {
#     route: "account",
#     access: [
#         "client",
#         "manager"
#     ]
# }


@router.get('/access', response_model=list[RouteBase])
def get_access(db: Session = Depends(get_db)):
    return get_access_db(db)