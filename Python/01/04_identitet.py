a = 123345677
b = 123345670 # probaj sa istom vrijednosti u startu, bez linije 4
print(id(a))
b += 7 # ista vrijednost
print(id(b))

if a is b:
    print("a i b imaju isti identitet")
if a == b:
    print("a i b imaju istu vrijednost")
if type(a) is type(b):
   print("a i b su istog tipa")
