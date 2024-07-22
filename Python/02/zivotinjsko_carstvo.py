class Animal:
    def __init__ (self, name):
        self.name = name
        self._species_ = "UNKNOWN"
        
    # if changed, it is a polymorphism
    def say(self, something):  
        print("%s %s says %s" % (self._species_, self.name, something))
    
    # if not changed, it is a reusability a.k.a DRY concept
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return "Animal[%s], name=%s" % (self._species_, self.name)
    
    # encapsulation
    def setSpecies(self, species):
        self._species_ = species
    
    def getSpecies(self):
        return self._species_

animal = Animal ("ime") 
print ("Ime zivotinje je %s" % animal.name)

class Dog(Animal):  # inheritance
    def __init__(self, name, race):
        super().__init__(name)  # DRY concept
        self.race = race
        self.setSpecies("Dog")

dog = Dog("pas", "avlijaner")
dog.say("nesto")
print ("Ime zivotinje je %s" % dog.name)

class Horse(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self._species_ = "Horse"

horse = Horse("Cetalj", "ridjan")
horse.say("njihaaa")

class Robot:
    def __init__(self, type_, serialNumber):
        self.type_ = type_
        self.SN = serialNumber
    
    def walk(self):
        print("Robot %s with S/N: %s IS WALKING" % (self.type_, self.SN))
    
    def say(self, robot_says):
        print("Robot %s with S/N: %s says: %s" % (self.type_, self.SN, robot_says))
robot = Robot("HODAJUCI", 123456)
robot.walk()

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._species_ = "Bird"
    
    def flap(self):
        print("%s flaps!" % self)
        
    def fly(self):
        self.flap()
        self.flap()
        self.flap()
        self._fly_()

    def _fly_(self):
        print("%s flies!" % self)

bird = Bird("Wilie")

class Penguin(Bird): # mulitiple inheritance, multilevel inheritance
    def __init__(self, name):
        super().__init__(name)
        self._species_ = "Penguin"
    
    def _fly_(self):  # method overwriting
        print("%s flies NOT!" % self)
    
    def eat(self):
        print("%s eats FISH" % self);

penguin = Penguin("Chilly Willie")

# polymorphism
animals = [dog, horse, robot, bird, penguin]
for animal in animals:
    animal.say("isto")
    print(animal)

print(Penguin.mro())  # Method Resolution Order

birds = [bird, penguin]
for _bird in birds:
    _bird.fly()  # which _fly_ method will be called?

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._species_ = "Elephant"

    def eat(self):
        print("%s eats tons of peanut!" % self);

elephant = Elephant("Ellie")

class WTFIsThis(Penguin, Elephant):  # multiple inheritance
    def __init__(self, name):
        super().__init__(name)
        self._species_ = self.__class__.__name__
    
    def say(self, what_="ahaiahrgh"):
     super().say(what_)  # extending the functionality

wtf = WTFIsThis("ChillyEllie")
print(wtf)
print(WTFIsThis.mro())
wtf.eat()
wtf.say()


