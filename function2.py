def person(name,age =20):
    print("Name is : ",name)
    print("Age is: ",age)
person("Bhavanshu")
person("Bhavanshu",19)

print("------------------")

def person(name,age):
    print("Name is : ",name)
    print("Age is : ",age)
person("Bhavanshu",age =13)
print("------------------")
# varible length argument
def sum(a,*b):
    c =a
    print(a)
    print(b)
    for i in b:
        c += i
    print(c)
sum(1,2,3,4,5)

