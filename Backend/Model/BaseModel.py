from pydantic import BaseModel,Field

class User(BaseModel):
    uuid:str
    username:str
    email:str
    password:str

class UserSchema(BaseModel):
    email:str=Field(...)
    username:str=Field(...)
    password:str=Field(...)
 
class PasswordSchema(BaseModel):
    data:str
    encrypted_password:str

class PinSchema(BaseModel):
    uuid:str
    data:str=Field(...)
    encrypted_pin:str=Field(...)

class Token(BaseModel):
    access_token: str
    token_type: str

class IP_Address(BaseModel):
    uuid:str
    Ip_address:str

    
