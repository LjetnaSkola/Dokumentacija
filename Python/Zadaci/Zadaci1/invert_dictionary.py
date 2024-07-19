def invert_dictionary(input_dict):
    inverted_dict = {}

    for key, value in input_dict.items():
        inverted_dict[value] = key

    return inverted_dict

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dictionary(original_dict)
print("Originalni rečnik:", original_dict)
print("Obrnuti rečnik:", inverted_dict)
