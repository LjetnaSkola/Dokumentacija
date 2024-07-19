def foo(skup1):
    skup2 = set()
    skup3 = set()
    for elem in skup1:
        if (type(elem) == int or type(elem) == float):
            skup2.add(elem)
        else:
            skup3.add(elem)
    return skup2, skup3

def main():
    print(foo({1,2,3, 2.3, 4.5, "a", "b", 'C'}))
if __name__ == "__main__":
    main()

