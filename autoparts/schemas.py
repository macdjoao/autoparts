from pydantic import BaseModel

# User

class User(BaseModel):
    user_name: str
    user_email: str

class CreateUser(User):
    user_password: str

class ReadUser(User):
    user_id: int

class DeleteUser(BaseModels):
    user_email: str

# Brand

class Brand(BaseModel):
    brand_name: str
    brand_code: str

class ReadBrand(Brand):
    brand_id: str

class DeleteBrand(BaseModels):
    brand_code: str

# Model

class Model(BaseModel):
    model_name: str
    model_code: str   
    brand_code: str

class ReadModel(Model):
    model_id: str

class DeleteModel(BaseModels):
    model_code: str

# Part

class Part(BaseModel):
    part_name: str
    part_code: str   
    part_price: str
    part_amount: str
    model_code: str

class ReadPart(Part):
    part_id: str

class DeletePart(BaseModels):
    part_code: str