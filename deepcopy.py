from numpy import *
arr=  array([1,2,3,5,6])
arr1 = arr.copy()
arr[2] = 9
print(id(arr))
print(id(arr1))
print(arr)
print(arr1)
