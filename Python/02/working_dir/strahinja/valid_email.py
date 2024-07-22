import re

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"


def valid_email(user):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if not re.match(EMAIL_REGEX, user.email):
                raise Exception("Invalid email")
            else:
                return f(*args, **kwargs)

        return wrapper

    return decorator
