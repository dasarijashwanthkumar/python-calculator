import string
import random

def password_generator(length):

    passwordCh = string.digits + string.ascii_letters + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(passwordCh)
    return password

length = int(input("Enter Password Length:"))
print("Password Generated =",password_generator(length))