from fastapi import APIRouter, Depends, HTTPException, Security
from app.utils.auth import get_user_by_email, create_user
from app.schemas.auth import ClientCreate, Login, UserOut, RefreshToken, SignIn
from app.schemas.profiles import ClientBase
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.auth_class import Auth
from app.database import get_db
from sqlalchemy.orm import Session


security = HTTPBearer()
auth_handler = Auth()
router = APIRouter(
    tags=["Authorization"],
    prefix="/auth",
)


@router.post('/signup', response_model=ClientBase)
def signup(user: ClientCreate, db: Session = Depends(get_db)):
    """ Регистрация пользователя (клиента) """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.post('/signin', response_model=SignIn)
def login(user: Login, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if (db_user is None):
        raise HTTPException(status_code=401, detail='Invalid email')
    if (not auth_handler.verify_password(user.password, db_user.password)):
        raise HTTPException(status_code=401, detail='Invalid password')
    access_token = auth_handler.encode_token(user.email)
    refresh_token = auth_handler.encode_refresh_token(user.email)
    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.get('/refresh_token', response_model=RefreshToken)
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}