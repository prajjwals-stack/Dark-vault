from config.db_connection import db
from config.config import USER_COLLECTION
from Model.BaseModel import UserSchema
import bcrypt
from passlib.context import CryptContext
from cryptography.fernet import Fernet
import jwt


SECRET_KEY = "mytokenispure"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Auth:
    def addUser(self,data:dict,uuid:str):
        if(self.checkUser(data['email'])):
            return "user already exists"
        key=Fernet.generate_key()
        Userdata={
            "email":data['email'],
            "username":data['username'],
            "password":pwd_context.encrypt(data['password']),
            "uuid":uuid,
            "key":key
        }
        db["user management"].insert_one(dict(Userdata))
        return "User added successfully"

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
    
    def Create_token(self,username:str):
        user=db[USER_COLLECTION].find_one({'username':username})
        UserUUID=user['uuid']
        payload={
        "uuid":UserUUID,
        "expire_time":ACCESS_TOKEN_EXPIRE_MINUTES 
        }
        return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    def get_current_user(self,token:str):
        payload= jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return payload['uuid']
        
