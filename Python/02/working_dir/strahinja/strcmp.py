def strcmp(str1, str2):
    if str1 == str2:
        return 0
    elif str1 < str2:
        return -1
    return 1


if __name__ == "__main__":
    print(strcmp("Dog", "Cat"))
    print(strcmp("Dog", "Dog"))
    print(strcmp("dog", "Dog"))
    print(strcmp("A", "B"))
