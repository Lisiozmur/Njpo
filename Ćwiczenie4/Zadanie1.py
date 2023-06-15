import shelve
import bcrypt

def load_salt():
    with shelve.open('users.db') as db:
        salt = db.get('salt')
    return salt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def authenticate(login, password):
    with shelve.open('users.db') as db:
        if login in db:
            stored_password = db[login]['password']
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
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

def register_user(login, password):
    hashed_password = hash_password(password)
    with shelve.open('users.db') as db:
        db[login] = {
            'password': hashed_password
        }
        db['salt'] = bcrypt.gensalt()

# Rejestracja użytkownika
register_user('admin', 'password123')

# Deklaracja funkcji secure_function po rejestracji użytkownika
@authorize('admin', 'password123')
def secure_function():
    print("Przyznano dostęp")

secure_function()
