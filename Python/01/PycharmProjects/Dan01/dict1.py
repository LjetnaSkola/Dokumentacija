from collections import OrderedDict
def reverse_order_of_dictionary(dictionary):
    # Print original dictionary
    print("The original dictionary:", dictionary)

    # Reverse the order using OrderedDict and reversed()
    reversed_dict = OrderedDict(reversed(list(dictionary.items())))

    # Print the reversed order dictionary
    print("The reversed order dictionary:", reversed_dict)
    return reversed_dict

#dict_example = {'who': 19, 'are': 6, 'you': 99}
#reverse_order_of_dictionary(dict_example)
