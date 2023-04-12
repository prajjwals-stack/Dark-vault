from pydantic import BaseModel,Field

class User(BaseModel):
    name: str=Field(...)

class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    password:str=Field(...)
 
class PasswordSchema(BaseModel):
    data:str
    encrypted_password:str

class PinSchema(BaseModel):
    data:str=Field(...)
    encrypted_pin:str=Field(...)

class Token(BaseModel):
    access_token: str
    token_type: str
