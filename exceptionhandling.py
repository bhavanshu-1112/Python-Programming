# exception handling
a = 5
b= int(input("enter the value of b : "))
try:
    print(a/b)
except Exception as e:
    print(e)
    print('hey ,you cannot divide by zero')
finally:
    print('do you know maths??')
print('bye')