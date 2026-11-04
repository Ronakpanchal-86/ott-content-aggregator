from src.core.security import create_access_token
import hashlib
import secrets

users = []


def hash_password(password):
    salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        600000
    ).hex()

    return f"{salt}${password_hash}"


def register_user(user):
    for existing_user in users:
        if (
            existing_user["email"] == user.email
            or existing_user["username"] == user.username
        ):
            return None

    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "email": user.email,
        "password_hash": hash_password(user.password)
    }

    users.append(new_user)

    return {
        "id": new_user["id"],
        "username": new_user["username"],
        "email": new_user["email"]
    }

def verify_password(plain_password, stored_password):
    salt, stored_hash = stored_password.split("$")

    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        plain_password.encode(),
        salt.encode(),
        600000
    ).hex()

    return new_hash == stored_hash


def login_user(email, password):
    for user in users:
        if user["email"] == email:
            if verify_password(password, user["password_hash"]):
                return {
                    "id": user["id"],
                    "username": user["username"],
                    "email": user["email"]
                }

    return None

def generate_login_token(user):
    access_token = create_access_token(
        data={"sub": user["email"]}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }