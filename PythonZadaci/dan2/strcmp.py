def __strcmp(str1, str2):
    if str1 == str2:
        return 0

    if str1 > str2:
        return -1
    else:
        return 1


def main():
    s1 = "a"
    s2 = "a"
    print(f"Result: {__strcmp(s2, s1)}")

    
if __name__ == "__main__":
    main()
