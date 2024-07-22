from serializacija_korisnika import read_from_file, write_to_file
from korisnik import Korisnik
from unique_email import unique_email
from valid_email import valid_email
import bcrypt


def hash_the_password(password):
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode("utf-8")


def verify_password(plain_password, hashed_password):
    password_byte_enc = plain_password.encode("utf-8")
    hash_byte_enc = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hash_byte_enc)


def verify(password, user):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print(user.__dict__)
            if not verify_password(password, user._password_hash):
                raise Exception("Incorrect password")
            return f(*args, **kwargs)

        return wrapper

    return decorator


if __name__ == "__main__":
    password = input("Unesite lozinku: ")

    john = Korisnik("johndoemail.com", password, 2)

    @unique_email(john)
    @valid_email(john)
    def write():
        write_to_file(john)

    write()
    johnRead = read_from_file()[-1]

    @verify(password, johnRead)
    def check_password():
        return print(johnRead)

    check_password()
