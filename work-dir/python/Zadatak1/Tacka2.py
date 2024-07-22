
def provjeri_da_li_je_broj (vrijednost):
    return isinstance(vrijednost, (int, float, complex))
    
def napravi_dva_skupa(skup):
    set_brojeva = set()
    set_ostalih = set()
    for vrijednost in skup:
        if (provjeri_da_li_je_broj(vrijednost)):
            set_brojeva.add(vrijednost)
        else:
            set_ostalih.add(vrijednost)
    return set_brojeva, set_ostalih
    
skup = {1,2.3, "Dejana", "Petak", (3 + 5j)}
brojevi, drugi_tipovi = napravi_dva_skupa(skup)
print("Skup brojeva: ")
print(brojevi)
print("Skup ostalih tipova: ")
print(drugi_tipovi)