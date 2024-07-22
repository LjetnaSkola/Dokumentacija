class Adder:
    def add(self, x, y):
        raise NotImplementedError


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        return x | y


if __name__ == "__main__":
    ladd = ListAdder()
    print(ladd.add(["a", 1], ["b", 2]))

    dadd = DictAdder()
    print(dadd.add({"banana": "yellow"}, {"orange": "orange"}))
