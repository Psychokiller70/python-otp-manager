import random
import time

class OTPManager:
    def __init__(self, expiry_seconds=300):
        self.otp = None
        self.expiry_time = None
        self.expiry_seconds = expiry_seconds

    def generate_otp(self):
        self.otp = ''.join(random.choices("0123456789", k=6))
        self.expiry_time = time.time() + self.expiry_seconds
        return self.otp

    def is_valid(self, input_otp):
        current_time = time.time()
        if current_time > self.expiry_time:
            return False
        return input_otp == self.otp

# Example
manager = OTPManager()
otp = manager.generate_otp()
print("OTP:", otp)

# Simulate user input
user_input = input("Enter OTP: ")
if manager.is_valid(user_input):
    print("OTP is valid!")
else:
    print("OTP is invalid or expired.")
