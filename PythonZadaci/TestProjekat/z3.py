def foo(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict
def main():
    d1 = {"hi": "there", 5: 15}
    print(f"{foo(d1)}")

if __name__ == "__main__":
    main()
