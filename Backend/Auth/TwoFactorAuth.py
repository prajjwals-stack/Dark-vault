import pyotp
import json
import qrcode
from fastapi import HTTPException


class OTP():
    def __init__(self):
        self.totp=pyotp.TOTP('JBSWY3DPEHPK3PXP')

    def generate_otp(self,username:str):
        print(self.totp) 
        x=pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name=f"{username}", issuer_name='Dark Vault LTD')
        return x

    def verify_otp(self,otp:str):
        print(otp)
        print(self.totp)
        x=self.totp.verify(otp)
        if(x==False):
            raise HTTPException(status_code=422, detail="wrong one time password entered")
        print(x)
        return x