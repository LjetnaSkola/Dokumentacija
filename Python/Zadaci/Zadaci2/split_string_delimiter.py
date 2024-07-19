def split_string_delimiter(input_string, delimiter):

    substrings = input_string.split(delimiter)
    return substrings

input_string = "apple,bannana,cherry"
delimiter = ","
substrings = split_string_delimiter(input_string, delimiter)
print("Original string: ", input_string)
print("Substrings: ", substrings)