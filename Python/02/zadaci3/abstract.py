from abc import ABC, abstractmethod

class Adder(ABC):
    @abstractmethod
    def add(self, x, y):
        pass
class ListAdder:
    def add(self,x,y):
        return x+y
class DictAdder:
    def add(self,x,y):
        newdict = x.copy()  
        newdict.update(y)   
        return newdict

def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list_adder = ListAdder()
    concatenated_list = list_adder.add(list1, list2)
    print("Concatenated list:", concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dictionary_adder = DictAdder()
    merged_dict = dictionary_adder.add(dict1, dict2)
    print("Merged dictionary:", merged_dict)

if __name__ == "__main__":
    main()