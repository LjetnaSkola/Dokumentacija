from paket.generator import brojac
brojevi = brojac(5)
kvadrati = [n * n for n in brojevi] 
kvad_recnik = {n: n*n for n in brojevi}
print(brojevi)
print(kvadrati)
print(kvad_recnik)