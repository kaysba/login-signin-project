import os
import hashlib

SALT = 16
ITERATIONS = 100_000
ALG = "sha256"


def hash_password(password):
    salt = os.urandom(SALT)
    dk = hashlib.pbkdf2_hmac(
        ALG,
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )
    return salt.hex(), dk.hex()


def verify_password(password, salt_hex, hash_hex):
    salt = bytes.fromhex(salt_hex)
    stored_hash = bytes.fromhex(hash_hex)

    new_hash = hashlib.pbkdf2_hmac(
        ALG,
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )

    return new_hash == stored_hash


def email_exists(users, email):
    for user in users.values():
        if user["email"] == email:
            return True
    return False


def create_registration(users):
    user = {
        "last_name": "",
        "first_name": "",
        "address": "",
        "email": "",
        "salt": "",
        "password_hash": ""
    }

    print("Please enter your registration information:\n")
    user["last_name"] = input("Please enter your last name:\n")
    user["first_name"] = input("Please enter your first name:\n")
    user["address"] = input("Please enter your address:\n")

    email = input("Please enter your email address:\n")
    while email_exists(users, email):
        email = input(f"The email address {email} is already used, please choose another one:\n")
    user["email"] = email

    password = input("Please set a password:\n")
    password_confirm = input("Password confirmation:\n")
    while password != password_confirm:
        password_confirm = input("Passwords do not match, please try again:\n")

    # ICI : on hash et on stocke SEL + HASH (pas le password)
    salt_hex, hash_hex = hash_password(password)
    user["salt"] = salt_hex
    user["password_hash"] = hash_hex

    new_id = max(users.keys()) + 1 if users else 0
    users[new_id] = user

    print("Registration successful!\n")


def login(users):
    print("Please enter your login information:\n")
    email = input("Please enter your email address:\n")
    password = input("Please enter your password:\n")

    for user in users.values():
        if user["email"] == email:
            if verify_password(password, user["salt"], user["password_hash"]):
                print("Login successful!")
                print(f"Welcome {user['first_name']} {user['last_name']}")
                return True
            else:
                print("Incorrect password.")
                return False

    print("Email not found.")
    return False

users = {}
choice = ""

while choice != "QUIT":
    print("Welcome, please sign up or log in\n")
    print("1. Sign up --- 2. Log in\n")
    choice = input("Your choice: ")

    match choice:
        case "1":
            create_registration(users)
        case "2":
            if login(users):
                break
        case "QUIT":
            break
        case _:
            print("Invalid choice.")
