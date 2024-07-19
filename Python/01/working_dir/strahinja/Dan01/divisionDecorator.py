def validate_division(f):
    def fn(*args, **kwargs):
        if any(type(x) not in (int, float) for x in args):
            raise Exception("Must divide numbers")
        if args[1] == 0:
            raise Exception("Cannot divide by zero")
        return f(*args, *kwargs)

    return fn


@validate_division
def divide(dividend, divisor):
    return dividend / divisor


if __name__ == '__main__':
    try:
        print(divide(18, 5))
    except Exception as e:
        print(e)

    try:
        print(divide(18, 0))
    except Exception as e:
        print(e)

    try:
        print(divide(18, "we"))
    except Exception as e:
        print(e)
