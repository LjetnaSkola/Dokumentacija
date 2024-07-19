
def zamijeni_key_value(rjecnik):
    novi_rjecnik = {}
    for key,value in rjecnik.items():
        novi_rjecnik[value] = key
    return novi_rjecnik

rjecnik = {1: 'D', 2: 'E', 3: 'J', 4: 'A', 5: 'N', 6: 'A'}
print("Prije zamjene: ", rjecnik)
novi_rjecnik = zamijeni_key_value(rjecnik)
print("Poslije zamjene: ", novi_rjecnik)
        