import bcrypt


class Korisnik:
    def __init__(self, email, password, role, dont_hash=False):
        self.email = email
        self.role = role
        if dont_hash:
            self._password_hash = password
        else:
            self._password_hash = hash_the_password(password)

    def __str__(self):
        return f"({self.email},{self._password_hash},{self.role})"


def hash_the_password(password):
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode("utf-8")


def verify_password(plain_password, hashed_password):
    password_byte_enc = plain_password.encode("utf-8")
    hash_byte_enc = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hash_byte_enc)
