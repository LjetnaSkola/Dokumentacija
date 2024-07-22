class Automobil:
    broj_automobila = 0 # atribut klase

    def __init__(self,boja,naziv):
        self.boja = boja  # atribut objekta
        self.naziv = naziv  # atribut objekta
        Automobil.broj_automobila += 1 #atribut klase

    def info(self):
        print("%s automobil %s boje "%(self.naziv,self.boja))

    def full_print(self, test=None):  # test je defaultni argument
        if test:
            print(test)
        self.info()
        print(f"Ukupan broj automobila: {Automobil.broj_automobila}")

Automobil("crvena", "stojadin").info()  # moze i ovako
a = Automobil("metalik zelena", "golf") # a moze i ovako
a.full_print() # koliko ce biti automobila?

