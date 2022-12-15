from sqlalchemy.orm import Session
from schemas import CreateUser
from auth import get_hashed_password
from services import get_user_by_email, generate_full_name
from models import User

# Create User
def create_user(db: Session, user: CreateUser):
    try:
        if get_user_by_email(db=db, email=user.email):
            return 'Esse email já está cadastrado.'
        hashed_password = get_hashed_password(user.password)
        new_user = User(
        first_name=user.first_name.capitalize(),
        last_name=user.last_name.capitalize(),
        full_name=generate_full_name(user.first_name, user.last_name),
        email=user.email,
        password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return 'Usuário cadastrado com sucesso.', new_user
    except Exception as exc:
        print(f'create_user: {exc}')
        return 'Erro na aplicação.'


# Read User
# Update User
# Delete User

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
