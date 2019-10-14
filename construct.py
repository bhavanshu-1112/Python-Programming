class Computer:
    def __init__(self,ram,cpu):
        self.R = ram
        self.C = cpu
    def Config(self):
        print(self.R,self.C)

c1 = Computer('i5',64)
c2 = Computer('i7',32)
