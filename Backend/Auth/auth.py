from config.db_connection import db
from config.config import USER_COLLECTION
from Model.BaseModel import UserSchema
import bcrypt
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Auth:
    def addUser(self,data:dict):
        
        data['password']=pwd_context.encrypt(data['password'])
        db["user management"].insert_one(dict(data))
        return data