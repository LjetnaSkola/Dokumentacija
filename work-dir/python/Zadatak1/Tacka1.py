
def ukloni_duplikate (lista):
    lista_bez_duplikata = set(lista)
    lista.clear()
    lista.extend(lista_bez_duplikata)

lista = [1,2,2,3,4,5,6,6,6,7]
print("Lista sa duplikatima: \n")
print(lista)
ukloni_duplikate(lista)
print("Uklonjeni duplikati: \n")
print(lista)
