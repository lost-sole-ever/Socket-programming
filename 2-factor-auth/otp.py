import pyotp
import time

key = "HaneelKumar"

totp = pyotp.TOTP(key)

print(totp.now())