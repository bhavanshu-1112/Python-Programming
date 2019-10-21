a= int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
try:
    print(a/b)
    k = int(input("enter the value of k"))
    print(k)
except ZeroDivisionError as e:
    print(e,"hi")
except ValueError as e:
    print(e,"hrllo")
except Exception as e:
    # print(e)
    print("Something went wrong",e)
finally:
    print('bye')
