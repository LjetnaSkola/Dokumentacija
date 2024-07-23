def foo(arr):
    nums = [n for n in arr if n > 0 and n <= 255 and type(n) == int]
    chars = [chr(n) for n in nums]
    return chars

def main():
    a = [65, 66, 67]
    print(f"{foo(a)}")


if __name__ == "__main__":
    main()
