c = [2, "string"]
a = [1,c,3,4,5,6]
b = list(a)
b[4] = 1000
c[0] = "string"
print(a)
print(b)
