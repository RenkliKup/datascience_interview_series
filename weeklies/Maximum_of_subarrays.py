
_array=[1, 2, 3, 1, 4, 5, 2, 3, 6]
_A=3

def find_Max_subarray(_array,_size):
    array=_array
    size=_size
    array_length=len(array)
    
    for i in range(array_length):
        if size+i<=array_length:
         yield max(array[i:size+i])

for i in find_Max_subarray(_array,_A):
    print(i,end=",")