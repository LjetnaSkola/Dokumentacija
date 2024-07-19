def foo(s):
    arr = []

    for char in s:
        arr.append(ord(char))
    return arr
def main():
    s = "String"
    print(foo(s))
if __name__ == "__main__":
    main()
