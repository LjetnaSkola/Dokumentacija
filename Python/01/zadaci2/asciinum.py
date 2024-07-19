# String to ASCII function
def string_to_ascii(string):
    # Initialize an empty array
    ascii_arr = []
    for char in string:
        # Function ord takes a character and converts it to ASCII value (decimal)
        ascii_arr.append(ord(char))
    return ascii_arr

#string = "Emanuela"
#new_arr = string_to_ascii(string)
#print(f"String '{string}' as ASCII: {new_arr}")
