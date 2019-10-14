def add(x,y):
    while(y!=0):
        carry = x&y
        x = x^y
        y = carry<<1
    return x
a = int(input("enter  a number : "))
b = int(input("enter a number : "))
print(add(a,b))
