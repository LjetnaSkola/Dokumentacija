def brojac(n): 
	i = 0
	while n > i:
		yield i 
		i += 1 
	return
    
for i in brojac(10):
    print(i)
