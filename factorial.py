def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
i=0
while i<=n:
    f = factorial(i)
    print(f)
    i+=1