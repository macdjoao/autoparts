from sqlalchemy.orm import Session
from models import User

def get_user_by_email(db: Session, user_email: str):
    try:
        if db.query(User).filter(User.user_email == user_email).first():
            return True
        return False
    except Exception as exc:
        print(f'get_user_by_email: {exc}')