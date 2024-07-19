def iskaz1():
    print("iskaz1")

def iskaz2():
    print("iskaz2")

def statement3():
    print("statement3")

def statement4():
    print("statement4")

a = True

if a:
	iskaz1()
	iskaz2() # konzistentna indentacija
else:
	statement3()
          statement4() # nekonzistentna indentacija (greska)
