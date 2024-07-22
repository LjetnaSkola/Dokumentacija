from abc import ABC, abstractmethod


class Adder(ABC):
    @abstractmethod
    def add(self, x, y):
        pass


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        result = x.copy()
        result.update(y)
        return result
