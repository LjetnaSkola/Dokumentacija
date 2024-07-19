def isPrime(a):
    counter = 0
    for i in range(2, a//2 + 1):
        if (a % i == 0):
            return False
    return True

def generator(a, b):
    while a < b:
        if(isPrime(a)):
            yield a
        a += 1
    return

def digitsSum(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())

def main():
    lista = [num for num in generator(1, 100) if digitsSum(num) % 7 == 0]
    print(lista)

if __name__ == "__main__":
    main()
