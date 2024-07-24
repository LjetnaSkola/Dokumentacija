from abc import ABC, abstractmethod

class Adder(ABC):
    """
    Klasa za dodavanje.
    
    """
    @abstractmethod
    def add(self, x, y):
        pass

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

