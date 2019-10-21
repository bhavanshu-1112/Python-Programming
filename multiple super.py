class A:
    def __init__(self):
        super().__init__()
        print('init of A')
    def f1(self):
        print('f1 is working')

class B():
     def  __init__(self):
         # super().__init__()
         print('init of B')
     def f2(self):
        print('f2 is working')
# class D:
#     def __init__(self):
#         print('init of D')
#
#     def f4(self):
#         print('fawff')

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)

        print('init of C')
    def f2(self):
        print('f3 is working')

# a1 = A()
c1 = C()
# a1.f1()
# b1.f2()
# b1.f1()