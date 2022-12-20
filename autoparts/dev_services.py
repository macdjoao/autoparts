from sqlalchemy.orm import Session
from database import get_db
from faker import Faker
from schemas import CreateUser
from crud import create_user

def generate_fake_user() -> CreateUser:
    fake = Faker()
    fname = fake.first_name()
    lname = fake.last_name()
    email = fake.ascii_safe_email()
    password = email
    fake_user = CreateUser(first_name=fname, last_name=lname, email=email, password=password)
    return fake_user

def inject_fake_users(db: Session):
    Faker.seed(0)
    for _ in range(5):
        fake_user = generate_fake_user()
        create_user(db=db, user=fake_user)
