def asciiNumbersOfString(stringIn):
    return [ord(x) for x in stringIn]

if __name__ == '__main__':
    print(asciiNumbersOfString("ABC abc!"))
