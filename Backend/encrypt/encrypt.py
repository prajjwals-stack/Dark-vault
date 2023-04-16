from cryptography.fernet import Fernet
from config.config import USER_COLLECTION
from config.db_connection import db
import base64




class Encryption():
    def Encrypt(value:str,uuid:str):
        user=db[USER_COLLECTION].find_one({"uuid":uuid})
        key=user["key"]
        print(key)
        value_bytes = value.encode()
        cipher = Fernet(key)
        # Encrypt the value using the cipher
        encrypted_value = cipher.encrypt(value_bytes)
        return encrypted_value
        