class Razlomak:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def __str__(self):
        return "" + str(self.x) + "/" + str(self.y)


    def __add__(self, other):
        if isinstance(other, Razlomak):
            
            lcd = 0
            for i in range(2, self.y*self.x):
                if i % self.y == 0 and i % other.y == 0:
                    lcd = i
                    break
            return Razlomak(int(self.x*lcd/self.y) + int(other.x*lcd/other.y), lcd)
        else:
             raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

            
    def __mul__(self, other):
        if isinstance(other, Razlomak):
            return Razlomak(self.x * other.x, self.y * other.y)
        else:
             raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))


def main():
    a = Razlomak(10, 3)
    b = Razlomak(5, 4)
    print(a)
    print(f"Added: {a + b}")
    print(f"Multiplied: {a * b}")


if __name__ == "__main__":
    main()
