def foo(dict1):
    dict2 = dict()
    for key, value in dict1.items():
        dict2[value] = key
    return dict2

def main():
    print(foo(dict({"jedan": 1, "dva": 2, "tri": 3})))
if __name__ == "__main__":
    main()
