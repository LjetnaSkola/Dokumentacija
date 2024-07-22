def is_palindrome(s):

    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())

    return cleaned_string == cleaned_string[::-1]

#input_string = "A man, a plan, a canal, Panama"
#result = is_palindrome(input_string)
#print("The string is a palindrome." if result else "The string is not a palindrome.")

if __name__ == "__main__":

	input_string = input("Enter a string to check if it's a palindrome: ")
	result = is_palindrome(input_string)
	print("The string is a palindrome." if result else "The string is not a palindrome.")