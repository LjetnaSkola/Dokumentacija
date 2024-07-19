def replaceWithChars(inputList):
    return [chr(int(x)) if type(x) in (int, float) and x < 128 else x for x in inputList]
if __name__ == '__main__':
    print(replaceWithChars([65, 97, 200]))