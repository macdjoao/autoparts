from sqlalchemy.orm import Session
from schemas import CreateUser
from auth import get_hashed_password
from gets import get_user_by_email
from models import User

# Create User
def create_user(db: Session, user: CreateUser):
    try:
        if get_user_by_email(db=db, user_email=user.user_email):
            return 'Esse email já está cadastrado'
        hashed_password = get_hashed_password(user.user_password)
        new_user = User(
        user_name=user.user_name,
        user_email=user.user_email,
        user_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as exc:
        print(f'create_user: {exc}')
        return 'Erro na aplicação'


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
