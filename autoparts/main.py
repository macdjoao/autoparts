from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas import CreateUser, ReadUser
from crud import create_user

app = FastAPI()


@app.get('/')
def home(db: Session = Depends(get_db)):
    return 'Olá mundo'

@app.post('/users/')
def post_user(user: CreateUser, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)