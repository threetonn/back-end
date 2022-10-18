from fastapi import APIRouter, Depends, HTTPException, Security
from app.models import User
from app.utils import auth
from app.schemas.auth import ClientCreate, Login, UserOut
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.auth_class import Auth
from app.database import get_db
from sqlalchemy.orm import Session


security = HTTPBearer()
auth_handler = Auth()
router = APIRouter(
    tags=["Authorization"],
)


@router.post('/signup', response_model=UserOut)
def signup(user: ClientCreate, db: Session = Depends(get_db)):
    """ Регистрация пользователя (клиента) """
    db_user = auth.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth.create_user(db=db, user=user)


@router.post('/signin')
def login(user: Login, db: Session = Depends(get_db)):
    db_user = auth.get_user_by_email(db, email=user.email)
    if (db_user is None):
        return HTTPException(status_code=401, detail='Invalid username')
    if (not auth_handler.verify_password(user.password, db_user.password)):
        return HTTPException(status_code=401, detail='Invalid password')
    access_token = auth_handler.encode_token(user.email)
    refresh_token = auth_handler.encode_refresh_token(user.email)
    return {'access_token': access_token, 'refresh_token': refresh_token}

@router.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}


@router.get('/me', response_model=UserOut)
def me(user: User = Security(auth.get_current_user)):
    return user