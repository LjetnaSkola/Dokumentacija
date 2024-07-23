from math import sqrt

def korutina():
    try:
        while True:
            gen = (yield)
            prev_diff = 8
            prev_num = 0
            for num in gen:
                for i in range(num - 6, num + 7):
                    diff = abs(i - num)
                    if(i % 7 == 0 and diff < prev_diff):
                        prev_diff = diff
                        prev_num = i
            print(f"Najblizi broj djeljiv sa 7 je: {prev_num}")
    
    except GeneratorExit:
        print("")
    
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range (2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

    
def gen(a, b):
    i = 1
    for i in range(a,b):
        if (is_prime(i)):
            yield i

    return

def main():
    a = 10
    b = 30
    prime_gen1 = gen(a,b)
    coroutine = korutina()
    next(coroutine)
    coroutine.send(prime_gen1)
    coroutine.close()

    prime_gen2 = gen(a,b)
    print(f"prime numbers between {a} and {b}:")
    for prime in prime_gen2:
        print(prime)


if __name__ == "__main__":
    main()
