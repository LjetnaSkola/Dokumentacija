def brojac(n):
	while n > 0:
		print("Stigao sam do %d"%n)
		yield n
		n -= 1
	return

print("rucno pozivanje next nad generatorom")
djenerator = brojac(10) # generator koji generise brojeve od 10 unazad
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
print(next(djenerator))
# print(next(djenerator)) # PRETJERAO ISPOD 1

print("for petlja od 20 na nize ")
for i in brojac(20):
    print(i)


print("suma brojaca do 5 ", sum(brojac(5)))