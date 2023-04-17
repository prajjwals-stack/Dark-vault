from cryptography.fernet import Fernet
from config.config import USER_COLLECTION
from config.db_connection import db


class Decryption(): 
    def Decrypt(encrypted_value:str,uuid:str):
        user=db[USER_COLLECTION].find_one({"uuid":uuid})
        key=user["key"]
        print(key)
        cipher = Fernet(key)
        decrypted_value_bytes = cipher.decrypt(encrypted_value)
        decrypted_value = decrypted_value_bytes.decode()
        return decrypted_value
        