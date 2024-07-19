from zadaci4.primeNumberGenerator import prime_from_to


def is_sum_of_digits_divisible_by7(x):
    return sum([int(i) for i in str(x)]) % 7 == 0


if __name__ == "__main__":
    print([x for x in prime_from_to(2, 100) if is_sum_of_digits_divisible_by7(x)])
