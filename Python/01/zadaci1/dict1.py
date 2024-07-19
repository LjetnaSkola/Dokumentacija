
from collections import OrderedDict

# Initialize dictionary
dict = {'who' : 19, 'are' : 6, 'you' : 99}
print("The original dictionary : " + str(dict))

# Using OrderedDict() + reversed() + items()
res = OrderedDict(reversed(list(dict.items())))
print("The reversed order dictionary : " + str(res)) 
