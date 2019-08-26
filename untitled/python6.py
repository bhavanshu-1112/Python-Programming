from array import *
arr = array('l',[1,-2,3,4])
print(arr)
print(type(arr))
print(arr.buffer_info())
for i in arr:
    print(i)
narr = array('l',[a*2 for a in arr])
print(narr)