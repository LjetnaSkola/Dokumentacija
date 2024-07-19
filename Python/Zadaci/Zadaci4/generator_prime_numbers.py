def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n // 2 - 1):
        if n % i == 0:
            return False
    return True


def prime_generator(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            yield num


start = 10
end = 50

for prime in prime_generator(start, end):
    print(prime)
