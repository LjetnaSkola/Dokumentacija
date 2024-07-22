def is_palindrome(string_input):
    return string_input[::-1] == string_input


def is_palindrome_ci(string_input):
    return string_input[::-1].upper() == string_input.upper()


if __name__ == "__main__":
    print(is_palindrome("anavolimilovana"))
    print(is_palindrome("AnavoliMilovana"))  # false
    print(is_palindrome_ci("AnavoliMilovana"))  # true
    print(is_palindrome("sys"))
    print(is_palindrome("Praksa"))
