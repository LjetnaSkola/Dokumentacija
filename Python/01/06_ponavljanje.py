a = [1,2,3] # a je lista brojeva
b = [a] # b je lista koja sadrzi referencu na a
c = b * 4 # c sadrzi 4 reference na a
print(c)
a[1] = 10000
print(c)