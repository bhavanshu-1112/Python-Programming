class A:
    def f1(self):
        print('h1 is working ')

class B(A):
    def f2(self):
        print('h2 is working')

class C(A):
    def f3(self):
        print('h3 is working')

a1 = A()
b1 = B()
c1 = C()
a1.f1()
b1.f1()
b1.f2()
c1.f1()
# c1.f2()
c1.f3()