def reverseDict(originalDict):
    return {y: x for x, y in originalDict.items()}

if __name__ == '__main__':
    print(reverseDict({'A': 1, 'B': 2, 'C': 3}))