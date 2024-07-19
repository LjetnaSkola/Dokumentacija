

# Podijeli string na podstringove gdje je delimiter zadati znak
# string.split(separator, maxsplit)

def razdvoji_string(string,separator):
    podstringovi = string.split(separator)
    return podstringovi
    
string = "Python, me, iznenadio."
print("Prije razdvajanja: ", string)
podstringovi = razdvoji_string(string, ',')
print("Poslije razdvajanja: ", podstringovi)
