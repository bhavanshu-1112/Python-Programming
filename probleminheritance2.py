class Base1(object):
    def __init__(self):
        self.str1 = "Animals"
        print("B1")


class Base2(object):
    def __init__(self):
        self.str2 = "Birds"
        print("B2")


class Derived(Base1, Base2):
    def __init__(self):

        Base1.__init__(self)
        print("Animals have eyes legs")
        Base2.__init__(self)
        print ("Birds have eyes legs")


    def printStr(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStr()
