def string_compare(str1,str2):
    if str1 < str2:
        print(str1 + " comes before " + str2 + " in the dictionary.")
        return -1
    elif str1 > str2:
        print(str1 + " comes after " + str2 + " in the dictionary.")
        return 1
    else:
        print(str1 + " and " + str2 + " are the same.")
        return 0
    
def main():
    str1 = "emanuela"
    str2 = "manuela"
    string_compare(str1,str2)

if __name__ == "__main__":
    main()