def decorator(func):
    def wrapper(a, b):
        if((type(a) in (int, float)) and (type(a) in (int, float)) and b > 0):
           return func(a,b)
        else:
            return "Ne moze se dijeliti"
    return wrapper

@decorator
def devide(a,b):
    return a/b


def main():
    print(devide(10,0))

if __name__ == "__main__":
    main()
