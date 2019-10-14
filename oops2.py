class Computer:
    def __init__(self):
        self.n = "DELL"
        self.a = 2016
    def Compare(self,c2):
        if self.a == c2.a:
            return True
        else:
            return False
    def update(self):
        self.a  =2019
c1 = Computer()
c2 = Computer()
if c1.Compare(c2):
    print("Same")
else:
    print("different")
c1.update()
print(c1.a,c2.a)
c2.n = "HP"
print(c1.n,c2.n)
