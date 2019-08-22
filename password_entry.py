"""
Tyler
"""

MIN_LENGTH = 2
MAX_LENGTH = 12

user_password = input("Enter password: ")
while len(user_password) < MIN_LENGTH or len(user_password) > MAX_LENGTH:
    print("Invalid Password")
    user_password = input("Enter password: ")

print("*" * len(user_password))