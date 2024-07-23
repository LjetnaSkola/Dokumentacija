from abc import ABCMeta, abstractmethod
class Adder:
    __metaclass__ = ABCMeta
    @abstractmethod
    def add(self, x: None , y: None):
        pass

        
class ListAdder(Adder):
    def add(self, x: list[None], y: list[None]):
        return x + y


class DictAdder(Adder):
    def add(self, x: dict[None, None], y: dict[None, None]):
        d = {}
        for key, val in x.items():
            d[key] = val
        for key, val in y.items():
            d[key] = val

        return d


def main():
    a = [0,2,3]
    b = [3,4,5]
    adder = ListAdder()
    print(f"{adder.add(a,b)}")
    c = {"1": 2}
    d = {"2": 1}
    adder = DictAdder()
    print(f"{adder.add(c,d)}")
    
if __name__ == "__main__":
    main()
