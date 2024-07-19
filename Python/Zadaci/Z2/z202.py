def palindrom(string):
    if(string[::] == string[::-1]):
        return True
    else:
        return False


def main():
    print(palindrom("ana"))
    print(palindrom("Kuca"))
if __name__ == "__main__":
    main()
