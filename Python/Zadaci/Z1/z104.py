def foo(dict1):
    keys = set()
    values = list()
    for key, value in dict1.items():
        keys.add(key)
        values.append(value)
    return keys, values


def main():
    print(foo(dict({"jedan": 1, "dva": 2, "tri": 3})))
if __name__ == "__main__":
    main()
