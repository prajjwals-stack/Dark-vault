from pydantic import BaseModel,Field

class User(BaseModel):
    name: str=Field(...)

class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    password:str=Field(...)
 
class PasswordSchema(BaseModel):
    data:str=Field(...)
    encrypted_password:str=Field(...)

class PinSchema(BaseModel):
    data:str=Field(...)
    encrypted_pin:str=Field(...)
