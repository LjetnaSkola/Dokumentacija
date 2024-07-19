def foo(array):
    array2 = [chr(elem) for elem in array if elem > 0 and elem < 255 and type(elem) == int]
    return array2

def main():
    array = [65, 66, 99, 100]
    print(foo(array))
if __name__ == "__main__":
    main()
