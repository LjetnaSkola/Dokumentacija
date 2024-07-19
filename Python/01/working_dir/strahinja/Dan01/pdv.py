from primeNumberGenerator import prime_from_to


def dodaj_pdv(dictIn):
    return {x: y * 1.17 for x, y in dictIn.items()}


if __name__ == "__main__":
    print(dodaj_pdv({"jagode": 12, "mlijeko": 2}))
