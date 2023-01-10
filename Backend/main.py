from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db_connection import db

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



