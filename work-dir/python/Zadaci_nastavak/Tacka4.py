# Napisati funkciju koja vrši poredjenje dva stringa poput strcmp().
# Funkcija vraca 0 ako su stringovi jednaki,
# -1 ako je prvi string veci od drugog i 1 ako je drugi string veći od prvog.

def strcmp_user_defined(string1, string2):
    if (len(string1) != len(string2)):
        return -1;
    for i in range(len(string1)):
        if string1[i] < string2[i]:
            return -1
        else:
            if string1[i] > string2[i]:
                return 1
    return 0

string1 = "Danas"
string2 = "Danas"
string3 = "Sutra"

if strcmp_user_defined(string1, string2) == 0:
    print(string1, string2, "su jednaki")
else:
    print(string1, string2, "nisu jednaki")

if strcmp_user_defined(string1, string3) == 0:
    print(string1, string3, "su jednaki")
else:
    print(string1, string3, "nisu jednaki")
