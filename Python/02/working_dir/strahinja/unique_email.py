from serializacija_korisnika import read_from_file


def unique_email(user):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if any(u.email == user.email for u in read_from_file()):
                raise Exception("Email not unique.")
            else:
                return f(*args, **kwargs)

        return wrapper

    return decorator
