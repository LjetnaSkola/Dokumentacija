class Kucica:
    def __init__(self):
        self.pas = None
        print("Kreirana kucica")
        
    def dodajPsa(self, pas):
        self.pas = pas
        print("dodat Pas [%s]"%pas.rasa)
    
    def oslusni(self):
        if self.pas is not None:
            self.pas.oglasiSe()
            
    def __del__(self):
        print("brisemo: kucicu")
    
 
class Pas:
    velicina_copora = 0
    
    def __init__(self, rasa):
        print("[%s] Kreiranje psa"% rasa)
        self.rasa = rasa
        Pas.velicina_copora += 1

    def oglasiSe(self):
        print("[%s] vau vau"% self.rasa)
    
    def __del__(self):
        print("brisemo: %s"%self.rasa)
        Pas.velicina_copora -= 1

pas = Pas("Avlijaner")
print("Velicina copora[kreiran Avlijaner]: %s" % Pas.velicina_copora)
pas.oglasiSe()
drugi_pas = Pas("Posavac")
print("Velicina copora[kreiran Posavac]: %s" % Pas.velicina_copora)
drugi_pas.oglasiSe()
pas = drugi_pas
print("Velicina copora[Avlijaner nema referencu, Posavac ima dvije]: %s" % Pas.velicina_copora)
del pas
print("Velicina copora[Avlijaner nema referencu, Posavac ima jednu]: %s" % Pas.velicina_copora)
del drugi_pas
print("Velicina copora[Avlijaner nema referencu, Posavac nema referencu]: %s" % Pas.velicina_copora)
pas = Pas("NaBaterije")
print("Velicina copora[Novi cuko]: %s" % Pas.velicina_copora)
niz_pasa = [pas]
print("Velicina copora[Novi cuko i niz]: %s" % Pas.velicina_copora)
del pas
print("Velicina copora[samo niz]: %s" % Pas.velicina_copora)

kucica = Kucica()
kucica.oslusni()
kucica.dodajPsa(niz_pasa[0])
kucica.oslusni()
del niz_pasa[0]
print("Velicina copora[nema u nizu, ali ima u Kucici]: %s" % Pas.velicina_copora)
del kucica.pas
print("Velicina copora[nema u nizu, nema ni u kucici]: %s" % Pas.velicina_copora)
del kucica
print("Velicina copora: %s" % Pas.velicina_copora)