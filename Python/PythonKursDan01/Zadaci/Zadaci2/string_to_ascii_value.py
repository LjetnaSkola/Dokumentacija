def string_to_ascii_values(input_string):

	ascii_values = [ord(char) for char in input_string]
	return ascii_values

input_string = "hello"
ascii_values = string_to_ascii_values(input_string)
print("Original string: ", input_string)
print("ASCII values: ", ascii_values)