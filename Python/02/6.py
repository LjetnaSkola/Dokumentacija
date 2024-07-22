# modul abc (Abstract Base Classes) ugrađen u Python za stvaranje apstraktnih klasa i metoda
from abc import ABC, abstractmethod

class Adder(ABC):   # Adder kao apstraktna klasa
    @abstractmethod # add kao apstraktna metoda
    def add(self, x, y):
        pass
        
class ListAdder(Adder):
    def add(self, x, y):
        return x + y  # Konkatenacija lista

class DictAdder(Adder):
    def add(self, x, y):
        # Spajanje dva rječnika u novi rječnik
        result = x.copy()
        result.update(y)
        return result


# Testiranje

list1 = ['Dobro', 'jutro',]
list2 = ['kako', 'ste', '?']
concatenated_list = ListAdder().add(list1, list2)
print("Concatenated list:", concatenated_list)  

dict1 = {
  1: 'Python', 
  2: 'dictionary', 
  3: 'example'
}
dict2 = {
  4: 'Java', 
  5: 'some', 
  6: 'text'
}
dictionary = DictAdder().add(dict1, dict2)
print("Dictionary :", dictionary)  
