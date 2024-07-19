def something(f):
	def debug(*args,**kwargs):
		print("Pozivam funkciju %s"%f.__name__)
		return f(*args,**kwargs)
	return debug

@something
def test():
	print("test funkcija", 4)

@something
def druga_funkcija():
	print("druga funkcija", 10)

def nemam_decorator():
    print("nemam dekorator", 15)

test()
druga_funkcija()

something(nemam_decorator)()