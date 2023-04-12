from config.db_connection import db
from config.config import USER_COLLECTION
from Model.BaseModel import UserSchema
import bcrypt
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Auth:
    def addUser(self,data:dict):
        if(self.checkUser(data['email'])):
            return "user already exists"
        data['password']=pwd_context.encrypt(data['password'])
        db["user management"].insert_one(dict(data))
        return data

    def checkUser(self,email:str)->bool:
        if(db[USER_COLLECTION].find_one({'email':email})):
            return True
        return False
    
    def UserCheck(self,username:str):
        if(db[USER_COLLECTION].find_one({'username':username})):
            return True
        return False

    def VerifyPassword(self,username:str,password:str):
        user=db[USER_COLLECTION].find_one({'username':username})
        hashed_password=user['password']
        if(pwd_context.verify(password,hashed_password)):
            return True
        return False
