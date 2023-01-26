from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
from config.db_connection import db
from Model.BaseModel import UserSchema
from Auth import auth_obj
from fastapi.encoders import jsonable_encoder

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


