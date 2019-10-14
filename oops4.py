# classmethod and staticmethod
class Student:
    total_marks = 100
    college = 'IIIT'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)

    @classmethod
    def into(cls):
        print(cls.total_marks,cls.college)

    @staticmethod
    def other():
        print("this is student class")

Student.into()
Student.other()
s1 = Student(70,50,90)
s2 = Student(60,40,80)
print(s1.avg(),s2.avg())
Student.into()
Student.other()
