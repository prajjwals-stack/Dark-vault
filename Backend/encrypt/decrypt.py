from cryptography.fernet import Fernet

key=b'Zxys5wxsQ-ihvn8pOhHb-hZLGJE2BcxfItWEexbYosA='

cipher = Fernet(key)

# Decrypt the value using the cipher



class Decryption():
    def Decrypt(encrypted_value:str):
        # cifer=new.AES(key,AES_MODE_CBC)
        decrypted_value_bytes = cipher.decrypt(encrypted_value)
        decrypted_value = decrypted_value_bytes.decode()
        return decrypted_value
        