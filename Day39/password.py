import string
import random

characters = list(string.ascii_letters + string.digits+"!@#$%^&*()") # create a list of all letters,digits and signs

def generate_password():
    password_length = int(input("Length of password"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)

    print(password)

option = input("generate password (yes/no)")

if option.lower() == 'yes':
    generate_password()
elif option.lower() == 'no':
    print("program ended")
    quit()
else: 
    print("Invalid input")
    quit()