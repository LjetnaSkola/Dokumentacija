
# Napraviti generator koji generiše sve proste brojeve između dva zadata broja.


# sa https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def prost_broj (n):
    from math import sqrt

    prime_flag = 0

    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

   

def generator_prostih_brojeva(od, do):
    for broj in range(od, do):
        if prost_broj(broj):
            yield broj

for prost in generator_prostih_brojeva(10, 20):
    print(prost)

print("****************")
prost_broj(13)