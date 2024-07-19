class Automobil: 
	broj_automobila = 0 # atribut klase 
    
	def __init__(self,boja,naziv): 
		self.boja = boja #atribut objekta 
		self.naziv = naziv #atribut objekta 
		Automobil.broj_automobila += 1 #atribut klase 
        
	def tockovi(self, brt):
		self.broj_tockova = brt

	def info(self): 
		print("%s automobil %s boje "%(self.naziv,self.boja))

a = Automobil("zeleni", "golf")
a.info()