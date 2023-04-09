from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
from config.db_connection import db
from Model.BaseModel import UserSchema, PasswordSchema,User
from Auth import auth_obj
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from encrypt.encrypt import Encryption
from encrypt.decrypt import Decryption
import os 
from config.config import PASSWORD_COLLECTION
from config.db_connection import db


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

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


    

@app.get('/')
async def home():
    return {"message":"welcome to dark vault"}



@app.post('/signup')
async def signup(data:UserSchema=Body(...)):
    newdata = jsonable_encoder(data)
    newdata=auth_obj.addUser(newdata)
    return newdata

@app.post('/login')
async def login(username:str, password:str):
    if(auth_obj.UserCheck(username)==False):
        raise Exception("Username doesnt exists")
    return {username,password}

@app.post('/add_credentials')
async def add_credentials(data:PasswordSchema=Body(...)):
    x=Encryption.Encrypt(data.encrypted_password)
    dict={
        "name":data.data,
        "password":x,
    }
    
    db[PASSWORD_COLLECTION].insert_one(dict)
    return x

@app.post('/get_credentials')
async def get_credentials(data:User=Body(...)):
    print(data.name)
    y=db[PASSWORD_COLLECTION].find_one({'name':data.name},{'_id': 0})
    x=Decryption.Decrypt(y["password"])
    return x
