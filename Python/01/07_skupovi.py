s1 = {1,2,3,4,1,5,1,6}
print("s1", s1)
s2 = {4,5,6,7,8,9}
print("s2", s2)
unija = s1 | s2
print("unija", unija)
presjek = s1 & s2
print("presjek", presjek)
razlika = s1 - s2
print("razlika s1 - s2", razlika)
razlika = s2 - s1
print("razlika s2 - s1", razlika)
sim_razlika = s1 ^ s2
print("simetricna razlika", sim_razlika)
