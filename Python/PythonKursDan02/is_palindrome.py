def is_palindrome(s):

    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())

    return cleaned_string == cleaned_string[::-1]

