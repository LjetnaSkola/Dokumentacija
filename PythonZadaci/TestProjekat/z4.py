def foo(dictionary):
    s1 = set()
    l1 = []
    for key,value in dictionary.items():
        s1.add(key)
        l1.append(value)
    return s1, l1
        
def main():
    d = {"key1": 2, "key2": 1}
    print(f"{foo(d)}")
if __name__ == "__main__":
    main()
