from fastapi import APIRouter, Depends, Security, UploadFile, File
from app.database import get_db
from sqlalchemy.orm import Session
from app.permissions import get_current_user
from app.models import User
from app.upload_image import handle_file_upload
from app.schemas.profiles import ClientBase, TrainerBase
from app.utils.profiles import get_trainer_profile

router = APIRouter(
    tags=["Profile"],
    prefix="/profile",
)


@router.post('/add_image', response_model=ClientBase)
async def add_image(db: Session = Depends(get_db), image: UploadFile = File(...), user: User = Security(get_current_user)):
    user.image = await handle_file_upload(id=user.id, file=image)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get('/me', response_model=TrainerBase | ClientBase)
def profile(user: User = Security(get_current_user)):
    if user.Role.name == "trainer":
        return get_trainer_profile(user=user)
    return user