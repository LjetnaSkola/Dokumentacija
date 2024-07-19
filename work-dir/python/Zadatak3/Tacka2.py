def provjeri_dijeljenje(funkcija):
    def provjeri_i_dijeli(broj1, broj2):
        if isinstance(broj1, (int, float)) and isinstance(broj2, (int, float)):
            if broj2 != 0:
                return funkcija(broj1, broj2)
            else:
                print("Dijeljenje sa nulom nije dozvoljeno.")
                return None
        else:
            print("Oba parametra moraju biti brojevi.")
            return None
    return provjeri_i_dijeli

@provjeri_dijeljenje
def dijeli(broj1, broj2):
    return broj1 / broj2 if broj2 != 0 else None

rezultat = dijeli(10, 2)
if rezultat is not None:
    print("Rezultat dijeljenja:", rezultat)

rezultat = dijeli(10, 0)
if rezultat is not None:
    print("Rezultat dijeljenja:", rezultat)
