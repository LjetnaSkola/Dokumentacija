def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            yield num


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


start = 10
end = 100

prime_numbers = [num for num in prime_generator(start, end) if sum_of_digits(num) % 7 == 0]

print(prime_numbers)
