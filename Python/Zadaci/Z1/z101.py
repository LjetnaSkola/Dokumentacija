def foo(list1):
    return list(set(list1))

def main():
    print(foo([1,2,3,2,"a", "a", "b"]))
if __name__ == "__main__":
    main()
