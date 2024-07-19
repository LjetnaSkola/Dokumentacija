import math

from zadaci1.prvi import removeDuplicates
from zadaci1.drugi import excludeNumbers
from zadaci1.treci import reverseDict
from zadaci1.cetvrti import split_keys_and_vals_from_dictionary
from zadaci2.zadaci2_prvi import replaceWithChars
from zadaci2.zadaci2_drugi import isPalindrome, isPalindromeCI
from zadaci2.zadaci2_treci import asciiNumbersOfString
from zadaci2.zadaci2_cetvrti import split
from zadaci4.primeNumberGenerator import prime_from_to
from zadaci4.area import get_area_fn
from zadaci4.divisionDecorator import divide
from zadaci4.nearestDivisibleBy7 import nearest_divisible_by_7
from zadaci5.pipelineFiles import filter_files, find_files, opener
from zadaci5.comprehensionWithPrimeNumberGenerator import is_sum_of_digits_divisible_by7
from zadaci5.pdv import dodaj_pdv


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2, 3, 4, 5, 5, "Aljosa", "Sergej", "Aljosa", {"name": "Alex", "age": 23}, {"name": "Alex", "age": 23}, {"name": "Sophia", "age": 22}]))

    print(excludeNumbers({"A", 'a', 1, 2, 3.5}))

    print(reverseDict({'A': 1, 'B': 2, 'C': 3}))

    print(split_keys_and_vals_from_dictionary({"name1": "friend", "age1": 23, "name2": "father", "age2": 55}))

    print(replaceWithChars([65, 97, 200]))

    print(asciiNumbersOfString("ABC abc!"))

    print(split("ABC abc !", " "))

    for x in prime_from_to(2, 100):
        print(x)

    print(f"Circle with radius 3.14 has area of: {get_area_fn("circle")(3.14)}")
    print(f"While pi^3 is: {math.pow(math.pi, 3)}")
    print(f"Square with side 5 has area of: {get_area_fn("square")(5)}")
    print(f"Rectangle 4x5 has area of: {get_area_fn("rectangle")(4, 5)}")

    try:
        print(divide(18, 5))
    except Exception as e:
        print(e)
    try:
        print(divide(18, 0))
    except Exception as e:
        print(e)
    try:
        print(divide(18, "we"))
    except Exception as e:
        print(e)

    coroutine = nearest_divisible_by_7()
    try:
        next(coroutine)
        print(coroutine.send(iter(range(100, 107))))
    except StopIteration:
        print("Not found in sequence")

    files = find_files(".")
    pyAndTextOnly = filter_files(files)
    for line in opener(pyAndTextOnly):
        print(line)

    print([x for x in prime_from_to(2, 100) if is_sum_of_digits_divisible_by7(x)])

    print(dodaj_pdv({"jagode": 12, "mlijeko": 2}))
