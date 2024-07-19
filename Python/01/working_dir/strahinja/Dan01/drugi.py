def excludeNumbers(originalSet):
    numbers = set([x for x in originalSet if type(x) in (int, float, complex)])
    return (numbers, originalSet - numbers)

print (excludeNumbers({"A", 'a', 1, 2, 3.5}))