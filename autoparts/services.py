from models import User
from sqlalchemy.orm import Session


def email_already_registered(db: Session, email: str):
    try:
        if db.query(User).filter(User.email == email).first():
            return True
        return False
    except Exception as exc:
        print(f'email_already_registered: {exc}')


def generate_full_name(first_name: str, last_name: str):
    try:
        fname = first_name.capitalize()
        lname = last_name.capitalize()
        full_name = f'{fname} {lname}'
        return full_name
    except Exception as exc:
        print(f'generate_full_name: {exc}')
        return 'Erro na aplicação.'
