from crud import create_user
from database import get_db
from fastapi import Depends, FastAPI
from schemas import CreateUser
from sqlalchemy.orm import Session

app = FastAPI()


@app.get('/', summary='Olá Mundo.')
def home(db: Session = Depends(get_db)):
    """Olá Mundo."""
    return 'Olá mundo.'


@app.post('/users/', summary='Cadastrar usuário.')
def post_user(user: CreateUser, db: Session = Depends(get_db)):
    """Rota para cadastro de usuário."""
    return create_user(db=db, user=user)
