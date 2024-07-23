class Animal:
    def __init__ (self, name):
        self.name = name

animal = Animal ("ime") 
print ("Ime zivotinje je %s" % animal.name)

class Dog(Animal):  # inheritance
    def __init__(self, name, race):
        super().__init__(name)  # DRY concept
        self.race = race
    
    def say(self, something):
        print("Dog %s says %s" % (self.name, something))

dog = Dog("pas", "avlijaner")
dog.say("nesto")
print ("Ime zivotinje je %s" % dog.name)

