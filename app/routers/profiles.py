from fastapi import APIRouter, Depends, Security, UploadFile, File, Request
from app.database import get_db
from sqlalchemy.orm import Session
from app.permissions import get_current_user
from app.models import User
from app.upload_image import handle_file_upload
from app.schemas.profiles import ClientBase, TrainerBase, EditUser, EditTrainer
from app.utils.profiles import get_trainer_profile, get_user_profile, edit_trainer_profile, edit_user_profile


router = APIRouter(
    tags=["Profile"],
    prefix="/profile",
)


@router.post('/add_image', response_model=TrainerBase | ClientBase)
async def add_image(
    request: Request,
    db: Session = Depends(get_db), 
    image: UploadFile = File(...), 
    user: User = Security(get_current_user)
    ):
    user.image = await handle_file_upload(id=user.id, file=image)
    db.add(user)
    db.commit()
    db.refresh(user)
    return get_trainer_profile(request, user) if user.Role.name == "trainer" else get_user_profile(request, user=user, db=db)


@router.get('/me', response_model=TrainerBase | ClientBase)
def profile(request: Request, user: User = Security(get_current_user), db: Session = Depends(get_db)):
    if user.Role.name == "trainer":
        return get_trainer_profile(request, user)
    return get_user_profile(request, user=user, db=db)


@router.put('/edit', response_model=TrainerBase | ClientBase)
def edit_profile(request: Request,new_data: EditTrainer | EditUser, db: Session = Depends(get_db), user: User = Security(get_current_user)):
    if user.Role.name == "trainer":
        user = edit_trainer_profile(db, user, new_data)
        return get_trainer_profile(request, user)
    else: 
        user = edit_user_profile(db, user, new_data)
        return get_user_profile(request, user=user, db=db)