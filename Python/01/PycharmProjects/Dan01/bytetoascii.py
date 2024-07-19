# Num array to be checked
def array_to_ascii(array):
    # Initialize an empty array
    ascii_arr = []
    for num in array:
        if(num>= 0 and num<=255 and isinstance(num, int)):
            ascii_arr.append(chr(num))
    return ascii_arr


#num_arr = [100,200,1000,1.5]
#num_arr = array_to_ascii(num_arr)
#print(num_arr)
