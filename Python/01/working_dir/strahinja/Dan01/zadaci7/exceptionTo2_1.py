from zadaci7.expected_type import expected_type


@expected_type(list)
def replaceWithChars(inputList):
    if any(type(x) != int or x >= 128 or x < 0 for x in inputList):
        raise Exception(f"Not a char")
    z = [chr(x) for x in inputList]
    if any(not str(x).isprintable() for x in z):
        raise Exception(f"A character is not printable")
    return z


if __name__ == '__main__':
    try:
        print(replaceWithChars([65, 97, 200]))
    except Exception as e:
        print(e)