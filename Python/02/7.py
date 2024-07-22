class Razlomak:
    def __init__ (self, brojilac, imenilac):
        self.brojilac = brojilac
        self.imenilac = imenilac
        
    def __str__(self): # ispisivanje u obliku razlomka
        print("razlomak = %s / %s" % (self.brojilac, self.imenilac))
    
    def __mul__(self, other): # mnozenje razlomaka
        novi_brojilac = self.brojilac * other.brojilac
        novi_imenilac = self.imenilac * other.imenilac
        return Razlomak(novi_brojilac, novi_imenilac)
        
    def __add__(self, other): # sabiranje razlomaka
        novi_imenilac = self.imenilac * other.imenilac
        novi_brojilac = novi_imenilac/self.imenilac*self.brojilac + novi_imenilac/other.imenilac*other.brojilac
        return Razlomak(novi_brojilac, novi_imenilac)
      
# Testiranje 
      
r1 = Razlomak(1,2) 
r2 = Razlomak(7,5) 

r1.__str__()
r2.__str__()

mul_result = r1.__mul__(r2)
mul_result.__str__()

add_result = r1.__add__(r2)
add_result.__str__()