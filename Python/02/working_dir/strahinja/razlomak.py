class Razlomak:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __mul__(self, other, /):
        b = other.b * self.b
        a = other.a * self.a
        return Razlomak(a, b)

    def __add__(self, other, /):
        b = other.b * self.b
        a = self.a * other.b + other.a * self.b
        return Razlomak(a, b)


if __name__ == "__main__":
    r = Razlomak(10, 2)
    print(r)
    print(Razlomak(10, 4) * Razlomak(1, 2))
    print(Razlomak(10, 4) + Razlomak(1, 2))
