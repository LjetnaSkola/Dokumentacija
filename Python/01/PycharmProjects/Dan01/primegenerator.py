# Function to check if number is prime number
def is_prime(num):
        if num <=1:
            return False
        for i in range(2,int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

# Defining prime number generator
def prime_num_gen():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

prime_nums = prime_num_gen()
n = int(input("Input the number of prime numbers you want to generate? "))
print("First",n,"Prime numbers:")
for _ in range(n):
    print(next(prime_nums))