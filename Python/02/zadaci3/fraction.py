class fraction:
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum
        # Print as self_num/self_denum)
    def __add__(self, other):
        self.sumOfNum = self.num + other.num
        self.sumOfDenum= self.denum + other.denum
        return fraction(self.sumOfNum, self.sumOfDenum)
    def __str__(self):
        return f"{self.num}/{self.denum}"
    def __mul__(self,other):
        self.mulNum = self.num*other.num - self.denum*other.denum
        self.mulDenum = self.num*other.denum + self.denum*other.num
        return fraction(self.mulNum, self.mulDenum)

def main(): 
    frac1 = fraction(10,2)
    frac2 = fraction(34,6)
    addition = frac1 + frac2
    print(f"Addition: {addition}")
    mul = frac1*frac2
    print(f"Multiplication: {mul}")

if __name__ == "__main__":
    main()