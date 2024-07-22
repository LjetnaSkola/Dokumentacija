def split_dict(input_dict):

    keys_set = set(input_dict.keys())
    values_list = list(input_dict.values())

    return keys_set, values_list    

original_dict = {'a': 1, 'b': 2, 'c': 3}
keys_set, values_list = split_dict(original_dict)
print("Original dictionary: ", original_dict)
print("Keys set: ", keys_set)
print("Values list: ", values_list)