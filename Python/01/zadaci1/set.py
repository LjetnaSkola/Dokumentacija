# Mixed set 
s={1,2, "Ema",3,4, 'A',5,6,"Test",2.5, 3.0}
print(s)

# Set of numbers
s1_numbers = {x for x in s if isinstance(x,(int,float))}
print(s1_numbers)

# Set of other types of data
s2_others = {x for x in s if not isinstance(x,(int,float))}
print(s2_others)