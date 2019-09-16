a =10
def gb():
    a = 15
    print("inside a : " ,a)
gb()
print("outside a : ", a)
print("--------------")
a = 10
def gb():
    global a

    a=15
    print("inside a: ",a)
gb()
print("outside a :",a)
print("--------------")
a = 10


def gb():
    a =12
    print("inside a: ", a)
    global a

    # a = 15
    # a = 12
    print("inside  global a: ", a)

gb()
a =13
print("outside a :", a)
print("--------------")
a = 10
print(id(a))
def gb():
    a =11
    print(id(globals()['a']))
    print("inside a : ",a)
    globals()['a'] = 15
gb()
print("outside : ",a)
