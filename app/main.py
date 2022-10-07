from fastapi import FastAPI
from app.database import database


app = FastAPI()

@app.on_event("startup")
async def startup():
    '''Установка соединения с БД'''
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    '''Разрыв соединения с БД'''
    await database.disconnect()


@app.post('/signup')
def signup():
    return 'Sign up endpoint'

@app.post('/login')
def login():
    return 'Login user endpoint'

@app.get('/refresh_token')
def refresh_token():
    return 'New token'

@app.post('/secret')
def secret_data():
    return 'Secret data'

@app.get('/notsecret')
def not_secret_data():
    return 'Not secret data'