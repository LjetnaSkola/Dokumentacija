from Z1 import z101, z102, z103, z104
from Z2 import z201, z202, z203, z204 
from Z4 import z401, z402, z403
def main():
    print("Zadaci 1")
    print(z101.foo([1,2,3,2,"a", "a", "b"]))
    print(z102.foo({1,2,3, 2.3, 4.5, "a", "b", 'C'}))
    print(z103.foo(dict({"jedan": 1, "dva": 2, "tri": 3})))
    print(z104.foo(dict({"jedan": 1, "dva": 2, "tri": 3})))

    print("\nZadaci 2")
    print(z201.foo([65, 66, 99, 100]))
    print(z202.palindrom("ana"))
    print(z203.foo("String"))
    print(z204.foo("Ovo je string", " "))

    print("\nZadaci 4")
    print(z401.devide(10,2))
    print(z402.closure("krug")(10))

    for i in z403.generator(1, 20):
        print(i)

    print("Korutina")
    cor = z403.corutine()
    next(cor)
    gen = z403.generator(15, 22)
    cor.send(gen)
if __name__ == "__main__":
    main()
