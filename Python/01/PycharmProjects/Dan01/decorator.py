# Defining decorator
def check_division(func):
    def input(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
            return func(a, b)
        else:
            raise ValueError("Check input data for division")
    return input

# Function to divide two numbers
@check_division
def divide(a, b):
    return a / b

try:
    # Normal function call
    result = divide(10, 2)
    print("Result of division:", result)

    # Divide by zero
    result = divide(10, 0)
    print("Result of division:", result)
except ValueError as e:
    print("Error:", e)

try:
    result = divide(10, '2')
    print("Result of division:", result)
except ValueError as e:
    print("Error:", e)