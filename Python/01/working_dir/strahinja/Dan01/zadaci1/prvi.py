def removeDuplicates(originalList):
    z = []
    # return set(originalList) # ne radi kad su elementi dictionary - unhashable
    for x in originalList:
        if (x not in z):
            z.append(x)
    return z

if __name__ == '__main__':
    print (removeDuplicates([1, 1, 2, 3, 4, 5, 5, "Aljosa", "Sergej", "Aljosa", {"name": "Alex", "age": 23}, {"name": "Alex", "age": 23}, {"name": "Sophia", "age": 22}]))
