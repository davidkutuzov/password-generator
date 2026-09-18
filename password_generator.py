import secrets
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    character = lowercase + uppercase + digits + symbols

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    password += [
        secrets.choice(character)
        for _ in range(length-4)
    ]

    secrets.SystemRandom().shuffle(password)
    return "".join(password)

try:
    length = int(input("How long should the password be? "))

    if length <= 0:
        print("Password length must be greater than 0.")
        exit()
    if length < 8:
        print("Password length must be at least 8.")
        exit()
        
    count = int(input("How many passwords do you want? "))

    if count <= 0:
        print("Number of passwords must be greater than 0.")
        exit()

except ValueError:
    print("Please enter a valid number.")
    exit()

for _ in range(count):
    password = generate_password(length)
    print(password)
