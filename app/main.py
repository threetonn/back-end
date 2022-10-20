from fastapi import FastAPI
from app.routers import auth, role, gender, example
from fastapi.middleware.cors import CORSMiddleware

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
app.include_router(role.router)
app.include_router(gender.router)

app.include_router(example.router)