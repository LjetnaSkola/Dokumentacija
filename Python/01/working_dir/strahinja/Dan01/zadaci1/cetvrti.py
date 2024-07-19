def split_keys_and_vals_from_dictionary(originalDictionary):
    return (set(originalDictionary.keys()), list(originalDictionary.values()))

if __name__ == '__main__':
    print(split_keys_and_vals_from_dictionary({"name1": "friend", "age1": 23, "name2": "father", "age2": 55}))
