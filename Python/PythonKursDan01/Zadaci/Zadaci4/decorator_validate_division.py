def validate_division(func):
    def wrapper(numerator, denominator):
        if not (isinstance(numerator, (int, float)) and isinstance(denominator, (int, float))):
            raise ValueError("Both numerator and denominator must be numbers.")
        if denominator == 0:
            raise ValueError("The denominator cannot be zero.")
        return func(numerator, denominator)

    return wrapper


@validate_division
def divide(numerator, denominator):
    return numerator / denominator


try:
    print(divide(10, 2))
    print(divide(10, 0))
    print(divide(10, 'a'))
except ValueError as e:
    print(e)