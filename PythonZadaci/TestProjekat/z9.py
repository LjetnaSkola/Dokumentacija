def check_validity(f):
    def wrapper(a, b):
        if not(isinstance(a, (int, float)) and isinstance(b,(int,float))):
            raise TypeError("Not numbers")
        if b == 0:
            raise ValueError("Division by zero")
        return f(a,b)
    return wrapper


@check_validity
def divide(a, b):
    return a/b;


def main():
    a = 5
    b = 2
    print(f"{divide(a,b)}")


if __name__ == "__main__":
    main()
