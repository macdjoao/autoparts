from auth import get_hashed_password
from models import User
from schemas import CreateUser
from services import email_already_registered, generate_full_name
from sqlalchemy.orm import Session


# Create User
def create_user(db: Session, user: CreateUser):
    try:
        if email_already_registered(db=db, email=user.email):
            return 'Esse email já está cadastrado.'
        hashed_password = get_hashed_password(user.password)
        new_user = User(
            first_name=user.first_name.capitalize(),
            last_name=user.last_name.capitalize(),
            full_name=generate_full_name(user.first_name, user.last_name),
            email=user.email,
            password=hashed_password,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return 'Usuário cadastrado com sucesso.', new_user
    except Exception as exc:
        print(f'create_user: {exc}')
        return 'Erro na aplicação.'


# Read User
def read_all_users(db: Session):
    try:
        users = db.query(User).all()
        if users:
            return users
        return 'Nenhum usuário cadastrado'
    except Exception as exc:
        print(f'read_all_users: {exc}')
        return 'Erro na aplicação.'


def read_user(db: Session, email: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            return user
        return f'Nenhum registro encontrado com o email {email}'
    except Exception as exc:
        print(f'read_user: {exc}')
        return 'Erro na aplicação.'


# Update User

# Delete User
def remove_user(db: Session, email: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            db.delete(user)
            db.commit()
            return f'Usuário {user.full_name} com email {user.email} deletado com sucesso.'
        return f'Nenhum registro encontrado com o email {email}'
    except Exception as exc:
        print(f'delete_user: {exc}')
        return 'Erro na aplicação.'


# Create Brand
# Read Brand
# Update Brand
# Delete Brand

# Create Model
# Read Model
# Update Model
# Delete Model

# Create Part
# Read Part
# Update Part
# Delete Part
