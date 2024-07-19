import math


def is_prime(num):
    return not any(num % i == 0 for i in range(2, math.floor(math.sqrt(num)) + 1))


def prime_from_to(from_num, to_num):
    for prime in [x for x in range(from_num, to_num + 1) if is_prime(x)]:
        yield prime


if __name__ == "__main__":
    for x in prime_from_to(2, 100):
        print(x)
