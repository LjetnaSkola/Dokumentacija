def foo(str1, delimiter):
    return str1.split(delimiter)

podstring = list()

def main():
    str1 = "Ovo je string"
    delimiter = " "
    print(foo(str1, delimiter))
if __name__ == "__main__":
    main()


