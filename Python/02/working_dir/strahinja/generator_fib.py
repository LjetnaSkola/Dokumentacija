def next_fib():
    num1 = 0
    num2 = 1
    while True:
        yield num2
        num2, num1 = num1 + num2, num2


if __name__ == "__main__":
    var = next_fib()
    print(var)
    print(next(var))
    print(next(var))
    print(next(var))
    print(next(var))
    print(next(var))
    print(next(var))
