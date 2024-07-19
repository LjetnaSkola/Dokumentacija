def remove_duplicates_and_return_list(original_list):
    # Print original list
    print("The original list is:", original_list)

    # Remove duplicates and create new list
    unique_list = list(set(original_list))

    # Print content of unique list
    print("The list without duplicates is:", unique_list)
    return unique_list

#list1 = [1, 2, 3, 4, 4, 5, 1]
#remove_duplicates_and_return_list(list1)
