from pydantic import BaseModel

# User

class User(BaseModel):
    name: str
    email: str

class CreateUser(User):
    password: str

class ReadUser(User):
    id: int

class DeleteUser(BaseModel):
    email: str

# Brand

class Brand(BaseModel):
    name: str
    code: str

class ReadBrand(Brand):
    id: str

class DeleteBrand(BaseModel):
    code: str

# Model

class Model(BaseModel):
    name: str
    code: str   
    brand_code: str

class ReadModel(Model):
    id: str

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
    id: str

class DeletePart(BaseModel):
    code: str