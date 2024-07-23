def foo(string):
    arr = [ord(c) for c in string]
    return arr
def main():
    str1 = "ABC"
    print(f"{foo(str1)}")
if __name__ == "__main__":
    main()
