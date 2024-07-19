def replace_numbers_with_ascii(input_list):

    for i in range(len(input_list)):

        if isinstance(input_list[i], int) and 0 <= input_list[i] <= 255:

            input_list[i] = chr(input_list[i])

    return input_list


input_list = [65, 'hello', 256, 97, 'world', 200, 300]
output_list = replace_numbers_with_ascii(input_list)
print("Original list:", input_list)
print("Modified list:", output_list)