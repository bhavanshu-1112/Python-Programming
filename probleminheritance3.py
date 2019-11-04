class Student:
    def __init__(self,rno):
        self.rno =23

    # def getroll(self):
    #     return self.rno

class Marks(Student):
    def __init__(self,rno,marks):
        super(Marks,self).__init__(rno)
        self.marks = 454
        print(marks)

    # def getmarks(self):
    #     return self.marks

class Sports:
    def __init__(self,sportsmarks):
        # super(Sports, self).__init__()
        self.sportsmarks = 56
        print(sportsmarks)
    #
    # def getsportsmarks(self):
    #     return self.sportsmarks

class Result(Sports, Marks):
    def __init__(self):
       # super(Result).__init__()
        Sports.__init__(self)
        Marks.__init__(self)
        # self.totalmarks = totalmarks

    def printtotal(self):
           print("Roll No is : " + self.rno, " Marks is : "  + self.marks, "Sports Marks is : " + self.sportsmarks)
           total = self.sportsmarks + self.marks
           print("total is : ", total)


res = Result()
res.printtotal()