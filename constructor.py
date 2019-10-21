class A:
    def __init__(self):
        print('init of A')
    def f1(self):
        print('f1 is working')

class B(A):
     def  __init__(self):
         super().__init__()
         print('init of B')
     def f2(self):
        print('f2 is working')

# a1 = A()
b1 = B()
# a1.f1()
# b1.f2()
# b1.f1()