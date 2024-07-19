def isPalindrome(stringInput):
    return stringInput[::-1] == stringInput
def isPalindromeCI(stringInput):
    return stringInput[::-1].upper() == stringInput.upper()

if __name__ == '__main__':
    print(isPalindrome("anavolimilovana"))
    print(isPalindrome("AnavoliMilovana")) #false
    print(isPalindromeCI("AnavoliMilovana")) #true
    print(isPalindrome("sys"))
    print(isPalindrome("Praksa"))