import sys
import hashlib
import secrets


def log_in(login, password): 
    salt = None
    hash = None
    with open('db.txt', 'r') as db:
        for line in db:
            row = line.split(',')
            if row[0] == login:
                salt = row[1].encode()
                hash = row[2]

    if salt == None or hash == None:
        print('User not found')
        return

    pw_hash = hashlib.scrypt(password=password, salt=salt, n=8, r=512, p=4, dklen=32).hex()
    if hash == pw_hash:
        print('Success')
    else:
        print('Incorrect password')
    
def register(login, password):
    salt = secrets.token_hex(32).encode()
    hash = hashlib.scrypt(password=password, salt=salt, n=8, r=512, p=4, dklen=32).hex()
    
    with open('db.txt', 'w') as f:
        f.write(f"{login},{salt.decode()},{hash}")


choice = int(input("1. Log in\n2. Register\n0. Exit\n"))
match choice:
    case 1:
        login = input("login: ")
        password = input("password: ").encode()
        log_in(login, password)
    case 2:
        login = input("login: ")
        password = input("password: ").encode()
        register(login, password)
    case 0:
        sys.exit(0)