def fib(x):
    if x==1:
      return 0
    elif x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)
n = int(input("enter the largest number of the series "))
i=1
while fib(i)<=n:

    print(fib(i))
    i = i+1

