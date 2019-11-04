class Bank:
    def __init__(self,name):
        self.name = name


    def getname(self):
        return self.name

class Employee(Bank):
    def __init__(self,name,empname,salary):
        super(Employee, self).__init__(name)
        self.empname = empname
        # self.salary = salary

    def getempname(self):
        return self.empname


class Customer(Bank):
    def __init__(self,name,customername,balance):
        super(Customer, self).__init__(name)
        self.customername = customername
        self.balance = balance

    def getcustname(self):
        return self.customername
    def getcustbalance(self):
        return self.balance

customer1 = Customer('Bank of baroda','Jai Moondra',453464)
print(customer1.getname(),customer1.getcustname(),customer1.getcustbalance())

employee1 = Employee('Bank of baroda','Bhavanshu Jain')
print(employee1.getname(),employee1.getempname())

