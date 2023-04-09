from cryptography.fernet import Fernet
import os


key=b'Zxys5wxsQ-ihvn8pOhHb-hZLGJE2BcxfItWEexbYosA='
# key=os.environ['KEY']

cipher = Fernet(key)




class Decryption():
    def Decrypt(encrypted_value:str):
        decrypted_value_bytes = cipher.decrypt(encrypted_value)
        decrypted_value = decrypted_value_bytes.decode()
        return decrypted_value
        