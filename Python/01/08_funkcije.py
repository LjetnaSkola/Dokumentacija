def funkcija(a, b=0):
	return a+b

print("proslijedjen je jedan parametar funkciji, a vrijednost je:", funkcija(4))

def printf(fmt,*args):
	print(fmt%args)

printf("Moje ime je %s i imam %d godina","Pero",20)

def printf2(*args): # može i ovako
    print(args[0]%args[1:])

printf2("Moje ime je %s i imam %d godina. Imam %d unucadi.","Mitar",90, 5)

def zbir_n_brojeva(*args): # args je ustvari kolekcija
    suma = 0
    for i in args:  # posto je kolekcija, mozemo kroz nju iterirati
        suma += i
    return suma

values=[1,2,3]
print("zbir n brojeva", zbir_n_brojeva(*values))  # ova zvjezdica se zove otpakivac i niz [1, 2, 3] pretvara u 1, 2, 3

def ispis_podataka(**kwargs):
    print("\ntip ulaznog podatka:",type(kwargs))

    for kljuc, vrijednost in kwargs.items(): # kao što enumerate daje indeks i vrijednost, tako i .items() daje kljuc i vrijednost
        print(f"{kljuc}: {vrijednost}")  # novi nacin formatireanja

ispis_podataka(uredjaj="TTTech Gateway", serijski_broj="S_TTT_0123546687", variant="US-4G", ID=1234567890)
ispis_podataka(Ime="Dragan", Prezime="Stojkovic", Nadimak="Piksi",
               Email="pixi@nomail.com", Drzava="Srbija", godine=55, Plata=9876543210)
# ali moze i ovako:
konfiguracija = {'server': 'localhost',
                 'port': 3306,
                 'user': 'root',
                 'password': 'NikoNeZna!234'}
ispis_podataka(**konfiguracija)  # i ovo je otpakivac koji pretvara u server='localhost', port=3306...

############################################################################
print("doubler1")
values=[1,2,3]
def doubler1(values): # ovo values nije isto kao i ovo prvo!!!
    for i, old_value in enumerate(values): # enumerate, vraca pojedinacno torku: indeks i vrijednost na tom indeksu
        values[i] = old_value * 2
    return values

print("values prije doubler1", values)
print("doubler1", doubler1(values))
print("values poslije doubler1", values)


print("doubler2")
values=[1,2,3]

def doubler2(values): # ovo values nije isto kao i ovo prvo!!!
    new_values = []
    for value in values:
        new_values.append(value * 2)
    return new_values

print("values prije doubler2", values)
print("doubler2", doubler2(values))
print("values poslije doubler2", values)

