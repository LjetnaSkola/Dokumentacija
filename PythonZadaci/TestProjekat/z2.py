def foo(old_set):
    set1 = set([n for n in list(old_set) if type(n) == int or type(n) == float])
    set2 = set([n for n in list(old_set) if type(n) != int and type(n) != float])
    return set1, set2


def main():
    a = {1,4,"hi", 2.4}
    print(f"{foo(a)}")

    
if __name__ == "__main__":
    main()

