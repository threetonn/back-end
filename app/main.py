from fastapi import FastAPI
from app.routers import auth, role, gender, example


app = FastAPI()

app.include_router(auth.router)
app.include_router(role.router)
app.include_router(gender.router)

app.include_router(example.router)