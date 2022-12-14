from sqlalchemy.orm import Session
from models import User

def get_user_by_email(db: Session, email: str):
    try:
        if db.query(User).filter(User.email == email).first():
            return True
        return False
    except Exception as exc:
        print(f'get_user_by_email: {exc}')