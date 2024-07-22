def palindrom(string):
    s = "".join(string.split(" "))
    reverse = s[::-1]
    if(s== reverse):
        return True
    else:
        return False

def main():
    str1 = "anavolimilo vana"
    str2 = "test"
    print(f"{palindrom(str1)}, {palindrom(str2)}")
if __name__ == "__main__":
    main()
