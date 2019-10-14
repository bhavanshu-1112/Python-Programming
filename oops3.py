# instance and class variables
class Car:
    wheels =5
    def __init__(self,n,m):
        self.name = n
        self.mil = m

c1 = Car("BMW",20)
c2 = Car("audi",45)
print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)
print(Car.wheels)
Car.wheels =6
print(Car.wheels)
print(c1.wheels)
c1.wheels=7
print(c1.wheels)
print(c2.wheels)
print(Car.wheels)
Car.wheels =9
print(Car.wheels)
print(c1.wheels)
print(c2.wheels)
