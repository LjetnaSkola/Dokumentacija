def brojac(n):
	while n > 0:
		yield n
		n -= 1
	return

def korutina():
	print("Cekam na podatak")
	try:
		while True:
			n = (yield)
			print("Primljeno %r"%n)
	except GeneratorExit:
		print("Kraj korutine")

djenerator = brojac(10)
krt = korutina()
next(krt) # moramo doci do yielda
krt.send(next(djenerator))
krt.send(next(djenerator))
krt.send("bilo sta, ne mora next generator")

# primjer filteringa pomocu korutine
def filter_parne():
    while True: # ne mora try-catch
        n = (yield)
        if n % 2 == 0:
            print("Parni broj: ", n)

filter = filter_parne()
next(filter) # moramo doci do yielda
for i in brojac(20):
    filter.send(i) # producer - consumer
    