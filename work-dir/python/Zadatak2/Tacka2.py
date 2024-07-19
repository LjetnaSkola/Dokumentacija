#Napraviti program koji provjerava da li je string palindrom


def je_li_palindrom(string):
     return string == string[::-1]
     #obrnem i provjerim jesu li isti
     
string = "RADAR"
string1 = "ana"
string2 = "Danas"
#print(je_li_palindrom(string))
if(je_li_palindrom(string)):
    print("String", string, " je palindrom")
if(je_li_palindrom(string1)):
    print("String", string1, " je palindrom")
if(je_li_palindrom(string2)):
    print("String", string, " je palindrom")
