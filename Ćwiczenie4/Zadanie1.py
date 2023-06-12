import shelve
import hashlib
import binascii
from os import urandom

def hash_password(password, salt):
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return pwdhash.decode('ascii')

def authenticate(login, password):
    with shelve.open('users.db') as db:
        if login in db:
            stored_password = db[login]['password']
            salt = db[login]['salt']
            hashed_password = hash_password(password, salt)
            if hashed_password == stored_password:
                return True
    return False

def authorize(login, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if authenticate(login, password):
                return func(*args, **kwargs)
            else:
                raise ValueError("Nieautoryzowany dostęp")
        return wrapper
    return decorator

@authorize('admin', 'password123')
def secure_function():
    print("Przyznano dostęp")
secure_function()