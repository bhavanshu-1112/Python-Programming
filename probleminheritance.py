class Person():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):
    def __init__(self, name, eid):

        super(Employee, self).__init__(name)
        self.empID = eid

    def isEmployee(self):
        return True

    def getID(self):
        return self.empID

emp = Employee("A1", "E1")
print(emp.getName(), emp.isEmployee(), emp.getID()) 
