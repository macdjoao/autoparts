from crud import create_user, read_all_users, read_user
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

@app.get('/users/', summary='Buscar todos os usuários.')
def get_all_users(db: Session = Depends(get_db)):
    """Rota para buscar todos os usuários cadastrados."""
    return read_all_users(db=db)

@app.get('/user/{email}', summary='Buscar usuário por email.')
def get_user(email: str, db: Session = Depends(get_db)):
    """Rota para buscar usuário por email."""
    return read_user(db=db, email=email)
