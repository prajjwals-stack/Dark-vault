import pyotp
import json
import qrcode


class OTP():
    def __init__(self):
        self.totp=pyotp.TOTP('JBSWY3DPEHPK3PXP')

    def generate_otp(self,username:str,password:str):
        print(self.totp) 
        x=pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name=f"{username}", issuer_name='Dark Vault LTD')
        image=qrcode.make(x)
        
        return x

    def verify_otp(self,otp:str):
        print(otp)
        print(self.totp)
        x=self.totp.verify(otp)
        print(x)
        return x