from pydantic import BaseModel,Field


class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    hashed_password:str=Field(...)
    mobile_number:str=Field(...)

class PasswordSchema(BaseModel):
    data:str=Field(...)
    encrypted_password:str=Field(...)

class PinSchema(BaseModel):
    data:str=Field(...)
    encrypted_pin:str=Field(...)
