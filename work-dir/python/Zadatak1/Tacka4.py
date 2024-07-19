
def razdvoji(rjecnik):
    lista = []
    skup = set()
    for key,values in rjecnik.items():
        skup.add(key)
        lista.append(values)
    return lista, skup

rjecnik = {1:'a', 2:'b', 3:'v'}
print("Rjecnik je: ", rjecnik);
lista, skup = razdvoji(rjecnik)
print("Lista je: ", lista)
print("Skup je: ", skup)