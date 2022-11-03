import os
from fastapi import HTTPException, UploadFile
import aiofiles
import uuid
import shutil


BASEDIR = os.path.dirname(__file__)


async def handle_file_upload(id: int, file: UploadFile) -> str:
    _, ext = os.path.splitext(file.filename)
    img_dir = os.path.join(BASEDIR, 'statics/media/', str(id))
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)
    os.makedirs(img_dir)
    content = await file.read()
    if file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(status_code=406, detail="Only .jpeg or .png  files allowed")
    file_name = f'{uuid.uuid4().hex}{ext}'
    async with aiofiles.open(os.path.join(img_dir, file_name), mode='wb') as f:
        await f.write(content)
    url = f"http://127.0.0.1:8000/static/media/{id}/{file_name}"
    return url