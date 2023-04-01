from cryptography.fernet import Fernet

key=b'Zxys5wxsQ-ihvn8pOhHb-hZLGJE2BcxfItWEexbYosA='

cipher = Fernet(key)




class Encryption():
    def Encrypt(value:str):
        # cifer=new.AES(key,AES_MODE_CBC)
        value_bytes = value.encode()

        # Encrypt the value using the cipher
        encrypted_value = cipher.encrypt(value_bytes)
        return encrypted_value
        