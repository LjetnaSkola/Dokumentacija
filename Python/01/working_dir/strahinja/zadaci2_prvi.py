def replaceWithChars(inputList):
    return [chr(int(x)) if type(x) in (int, float) and x < 128 else x for x in inputList]

print(replaceWithChars([65, 97, 200]))