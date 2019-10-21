class A:
    def f1(self):
        print('f1 is warning')
class B(A):
    def f2(self):
        print('f2 is working')

a1 = A()
b1 = B()
a1.f1()
b1.f1()
b1.f2()
