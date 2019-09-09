def info():
    print("Hello IIIT")
info()
print("------------------")
def add():
    a =5
    b =6
    c= a+b
    print(c)
add()
print("------------------")

def add1():
    d = 5
    e =6
    f = d+e
    return f
r1 = add1()
print(r1)

def op():
    a = 5
    b = 6
    c = a*b
    d = b-a
    return c,d
r1,r2 = op()
print(r1)
print(r2)
print("------------------")

def update(x):
    x= 8
    print(x)
a= 10
update(a)
print(a)
print("------------------")

def update(x):
    print(id(x))
    x =8
    print(id(x))
    print(x)
a=10
print(id(a))
update(a)
print(id(a))
print(a)
print("------------------")

def update(list):
    print(id(list))
    print(list)
    # list[1] = 11
    list[:4] = [2,445,56,3]
    # list = [100,23,4546,34]
    print(id(list))
    print("Inner List:",list)
list = [1,5,9,10]
print("Outer list:",list)
print(id(list))
update(list)
print(id(list))