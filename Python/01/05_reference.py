a = 37 # novi objekat
b = a # povecava broj referenci - a i b pokazuju na 37
c = []
c.append(b) # povecava broj referenci jer c[0] pokazuje na 37
b = 4 # smanjuje broj referenci na vrijednost 37, jer b sada pokazuje na nesto drugo
print("reference na stringove")
s = "qwerty"
s1 = s
print(id(s), id(s1))
s = "abcde"
print(id(s))
print(s1)
print(s)

print("kopiranje struktura podataka")
a = [1,2,3,4,5,6]
# b = a
b = list(a) # otkomentarisati liniju iznad, a ovu zakomentarisati
b[4] = 1000
print(a)
print(b)
