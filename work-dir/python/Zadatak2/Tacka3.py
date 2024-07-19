# Napraviti program koji od stringa pravi niz brojeva
# gdje svaki broj odgovara ASCII vrijednosti datog karaktera

def pravi_niz_brojeva(string):
    niz = list(string.encode('ascii'))
    return niz
    
string = "DanasCemoOd8:00RaditiPython"
niz = pravi_niz_brojeva(string)
print("String:", string)
print("Niz:", niz)

# Pomoc:
# https://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python