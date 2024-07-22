def split_set(input_set):
    number_set = set()
    other_set = set()

    for item in input_set:
        if isinstance(item, (int, float)):
            number_set.add(item)
        else:
            other_set.add(item)

    return number_set, other_set

input_set = {1, 2.5, "Hello", 3, "world", True, (1, 2)}
number_set, other_set = split_set(input_set)
print("Original set: ", input_set)
print("Number set: ", number_set)
print("Other set: ", other_set)
