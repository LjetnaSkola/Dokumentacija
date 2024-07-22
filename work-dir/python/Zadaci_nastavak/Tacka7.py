from math import gcd

class Razlomak:
    def __init__(self, brojilac, imenilac):
        if imenilac == 0:
            raise ValueError("Imenioc ne može biti nula.")
        self.brojilac = brojilac
        self.imenilac = imenilac
        self._skrati()

    def _skrati(self):
        common_divisor = gcd(self.brojilac, self.imenilac)
        self.brojilac //= common_divisor
        self.imenilac //= common_divisor

    def __str__(self):
        if self.imenilac == 1:
            return str(self.brojilac)
        else:
            return f"{self.brojilac}/{self.imenilac}"

    def __mul__(self, other):
        if isinstance(other, Razlomak):
            return Razlomak(self.brojilac * other.brojilac, self.imenilac * other.imenilac)
        elif isinstance(other, int):
            return Razlomak(self.brojilac * other, self.imenilac)
        else:
            raise TypeError("Nepodržana operacija.")

    def __add__(self, other):
        if isinstance(other, Razlomak):
            novi_imenilac = self.imenilac * other.imenilac
            novi_brojilac = (self.brojilac * other.imenilac) + (other.brojilac * self.imenilac)
            return Razlomak(novi_brojilac, novi_imenilac)
        elif isinstance(other, int):
            return Razlomak(self.brojilac + other * self.imenilac, self.imenilac)
        else:
            raise TypeError("Nepodržana operacija.")


if __name__ == "__main__":
    r1 = Razlomak(3, 4)
    r2 = Razlomak(1, 2)

    print(f"r1 = {r1}")  # Ispisuje: r1 = 3/4
    print(f"r2 = {r2}")  # Ispisuje: r2 = 1/2

    r3 = r1 * r2
    print(f"r1 * r2 = {r3}")  # Ispisuje: r1 * r2 = 3/8

    r4 = r1 + r2
    print(f"r1 + r2 = {r4}")  # Ispisuje: r1 + r2 = 5/4
