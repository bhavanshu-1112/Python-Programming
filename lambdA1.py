from functools import reduce
#def is_even(n):
   # return n%2==0
num=[5,6,8,9,11]
even=list(filter(lambda n:n%2==0,num))
print(even)
double=list(map(lambda n:n*2,num))
print(double)
s=reduce(lambda a,b:a+b,num)
print(s)