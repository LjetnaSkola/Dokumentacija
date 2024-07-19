def reverseDict(originalDict):
    return {y: x for x, y in originalDict.items()}

print(reverseDict({'A': 1, 'B': 2, 'C': 3}))