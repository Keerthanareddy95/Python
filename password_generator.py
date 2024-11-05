import random
import string

def generate_password(length=12): #default length of 12
    if length < 4:
        raise ValueError("Password should be at least 4 characters in length!")
    
    # Defining character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensuring the password has atleast one of each type of character
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Filling rest of the password with random choices
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    #shuffle password
    random.shuffle(password)

    # convert list to string
    return ''.join(password)

#user input
password_length = int(input(" Enter length of the password (min length of 4): "))
try:
    print("Generated Password: ", generate_password(password_length))
except ValueError as e:
    print(e)