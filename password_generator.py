import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
try:
    length = int(input("How long should the password be? "))

    if length <= 0:
        print("Password length must be greater than 0.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()
  
password = "".join(secrets.choice(characters) for _ in range(length))

print("Your password: ", password)
