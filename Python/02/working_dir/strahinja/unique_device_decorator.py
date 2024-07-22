from uredjaj_from_file import readFromFile


def is_unique(dev):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if __check_unique(dev):
                return f(*args, **kwargs)
            else:
                print("Error: device is not unique")

        return wrapper

    return decorator


def __check_unique(dev):
    if any(dev.snum == d.snum or dev.uid == d.uid for d in readFromFile()):
        return False
    return True
