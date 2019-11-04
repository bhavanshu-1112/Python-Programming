from numpy import *
arr=  array([1,2,3,5,6])
arr1 = arr.view()
arr[1] = 7

print(arr)
print(arr1)
print(id(arr))
print(id(arr1))