
#Napraviti program koji od zadatog niza pronalazi 
#elemente koji su brojevi ne veći od jednog bajta i 
#zamjenjuje te brojeve sa njihovom ASCII vrijednosti, 
#odnosno karakterom

def nadji_zamijeni_ascii_vrijednoscu(lista):
    novi_niz = []
    for el in lista:
        if(el <= 255 and el >= 0 and isinstance(el, int)):
            novi_niz.append(chr(el))
    return novi_niz

niz = {1,2,3,4,5,289,3333333,1.6}
print("Originalni niz:", niz)
mod_niz = nadji_zamijeni_ascii_vrijednoscu(niz)
print("Modifikovani niz:", mod_niz)