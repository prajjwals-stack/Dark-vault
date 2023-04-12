import pyotp
import json
from twilio.rest import Client
SECRET_KEY="OTP VERIFICATION SECRET KEY"
ACCOUNT_SID='AC59d3f00185344ca7c80e290bc8bc0164'
AUTH_TOKEN='73699ff878b5f367485ba0f0979f1cd7'

TARGET_MOBILE_NUMBER='+916261909030'

client=Client(ACCOUNT_SID,AUTH_TOKEN)

class OTP():
    def __init__(self):
        # self.totp=pyotp.TOTP('base32secret')
        self.totp=pyotp.totp.TOTP('MY KEY').provisioning_uri(name='prajjwal', issuer_name='Dark Vault LTD')

    def generate_otp(self,number:str):
        print(type(self.totp)) 
        x=self.totp
        # message = client.messages.create(body=f"Your OTP for verification on Dark Vault is {x}",from_='+15076827113',
        # to='+918651297204')
        return x

    def verify_otp(self,otp:str):
        print(otp)
        x=self.totp.verify(otp)
        print(x)