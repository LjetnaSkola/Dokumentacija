from abc import ABC, abstractmethod


class Adder(ABC):
    @abstractmethod
    def add(self, x, y):
        """
        Metoda za dodavanje.
        :param x:
        :param y:
        :return:
        """
        pass


class ListAdder(Adder):
    def add(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        return x + y

    def add(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        result = x.copy()
        result.update(y)
        return result


adder = ListAdder()

# Access docstring for ListAdder class
print("Docstring for ListAdder class:")
print(adder.__class__.__doc__)

# Access docstring for ListAdder.add method (the last defined one)
print("\nDocstring for ListAdder.add method:")
print(adder.add.__doc__)
