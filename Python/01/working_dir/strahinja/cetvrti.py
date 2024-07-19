def splitKeysAndValsFromDIctionary(originalDictionary):
    return (set(originalDictionary.keys()), list(originalDictionary.values()))

print(splitKeysAndValsFromDIctionary({"name1": "friend", "age1": 23, "name2": "father", "age2": 55}))