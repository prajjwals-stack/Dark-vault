from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
from config.db_connection import db
from Model.BaseModel import UserSchema, PasswordSchema
from Auth import auth_obj
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from encrypt.encrypt import Encryption
from encrypt.decrypt import Decryption
import os 

key_str=b'\xc3~n.\xb4\x84Q\x8bK \x81\x15{\xe7\xe1\xe9"`?U\xb7\x8f\xb2\xed\xa31+m\x02\xcf+\xed'
# key = key_str.encode('utf-8')
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
    )

@app.get('/')
async def home():
    return {"message":"welcome to dark vault"}



@app.post('/signup')
async def signup(data:UserSchema=Body(...)):
    newdata = jsonable_encoder(data)
    newdata=auth_obj.addUser(newdata)
    return newdata

@app.post('/add_credentials')
async def add_credentials(data:PasswordSchema=Body(...)):
    x=Encryption.Encrypt(data.data)
    print(data.data)
    return x

@app.post('/get_credentials')
async def get_credentials(encrypted_value=Body(...)):
    x=Decryption.Decrypt(encrypted_value)
    return x
