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


def corutine():
    try:
        while True:
            n = (yield)
            prevDiff = 100000;
            prevNum = 1;
            for num in n:
                for i in range(num - 6, num + 7):
                    diff = abs(i - num)
                    if (i % 7 == 0 and diff < prevDiff):
                        prevDiff = diff
                        prevNum = i
            print(prevNum)
    except GeneratorExit:
        print("Kraj rutine")

def main():
    for i in generator(1, 20):
        print(i)

    print("Korutina")
    cor = corutine()
    next(cor)
    gen = generator(15, 22)
    cor.send(gen)
if __name__ == "__main__":
    main()
