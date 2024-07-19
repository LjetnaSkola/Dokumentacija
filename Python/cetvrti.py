def makeInc(x): 
	def inc(y): 
		return x+y 
	return inc 
inc10 = makeInc(10) 
print(inc10(1))
