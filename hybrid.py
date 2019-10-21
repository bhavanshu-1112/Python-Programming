class A:
    def f1(self):
        print('f1 is working')

class B(A):
    def f2(self):
        print('f2 is working')

class C(A):
    def f3(self):
        print('f3 is working')
class D(B,C):
    def f4(self):
        print('f4 is working')
        print("hi ! python")



a1 = A()
b1 = B()
c1 = C()
d1 =D()
a1.f1()
b1.f1()
b1.f2()
c1.f1()
# c1.f2()
c1.f3()
d1.f1()
d1.f2()
d1.f3()
d1.f4()