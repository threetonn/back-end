from fastapi import FastAPI
from app.routers import auth, profiles, role, gender, example, workout_type, workout, gym, users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os


BASEDIR = os.path.dirname(__file__)


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

app.include_router(profiles.router)

app.include_router(users.router)

app.include_router(role.router)
app.include_router(gender.router)
app.include_router(workout_type.router)

app.include_router(gym.router)
app.include_router(workout.router)

app.include_router(example.router)

app.mount("/static", StaticFiles(directory=BASEDIR + "/statics"), name="static")