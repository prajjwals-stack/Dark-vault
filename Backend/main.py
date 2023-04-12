from fastapi import FastAPI,Body,HTTPException,Depends
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
import jwt
from typing import Annotated
from Auth import otp_obj


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

SECRET_KEY = "mytokenispure"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

    

@app.get('/')
async def home():
    return {"message":"welcome to dark vault"}


@app.post('/signup')
async def signup(data:UserSchema=Body(...)):
    newdata = jsonable_encoder(data)
    newdata=auth_obj.addUser(newdata)
    otp_obj.generate_otp(data.username,data.password)
    return newdata

@app.post('/login')
async def login(formdata:OAuth2PasswordRequestForm=Depends()):
    if(auth_obj.UserCheck(formdata.username)==False):
        raise HTTPException(status_code=404,detail="user does not exist")
    if(auth_obj.VerifyPassword(formdata.username,formdata.password)==False):
        raise HTTPException(status_code=401,detail="wrong credentials")
    user_obj={
        "username":formdata.username,
    }
    token=jwt.encode(user_obj,SECRET_KEY)
    return {
        "access_token":token,
        "token_type":"bearer",
    }

@app.post('/add_credentials')
async def add_credentials(data:PasswordSchema=Body(...),token: str=Depends(oauth2_scheme)):
    x=Encryption.Encrypt(data.encrypted_password)
    dict={
        "name":data.data,
        "password":x,
    }
    
    db[PASSWORD_COLLECTION].insert_one(dict)
    return "successfully added password"

@app.post('/get_credentials')
async def get_credentials(data:User=Body(...),token: str=Depends(oauth2_scheme)):
    print(data.name)
    y=db[PASSWORD_COLLECTION].find_one({'name':data.name},{'_id': 0})
    if(y==None):
        raise HTTPException(status_code=404,detail="data not found")
    x=Decryption.Decrypt(y["password"])
    return x

@app.post('/verify_otp')
async def verify_otp_mobile(otp:str):
    return otp_obj.verify_otp(otp)
    