import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("How long should the password be? "))

password = "".join(secrets.choice(characters) for _ in range(length))

print("Your password: ", password)
