from pydantic import BaseModel

# User


class User(BaseModel):
    first_name: str
    last_name: str
    email: str


class CreateUser(User):
    password: str


class ReadUser(User):
    email: int


class DeleteUser(BaseModel):
    email: str


# Brand


class Brand(BaseModel):
    name: str
    code: str


class ReadBrand(Brand):
    code: str


class DeleteBrand(BaseModel):
    code: str


# Model


class Model(BaseModel):
    name: str
    code: str
    brand_code: str


class ReadModel(Model):
    code: str


class DeleteModel(BaseModel):
    code: str


# Part


class Part(BaseModel):
    name: str
    code: str
    price: str
    amount: str
    model_code: str


class ReadPart(Part):
    code: str


class DeletePart(BaseModel):
    code: str
