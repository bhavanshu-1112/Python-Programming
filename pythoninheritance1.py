class Temperature:
    def __init__(self,name):
       self.name = name

    def getname(self):
        return self.name

    def isinDanger(self):
        return False

class City(Temperature):

    def __init__(self,name, tempcity):
        super(City, self).__init__(name)
        self.tpcity = tempcity

    def gettempcity(self,tempcity):
        if tempcity > 50:
           print('City is very hot')
           def isinDanger(self):
               return True


        elif tempcity < 10:
            print('City is very cold')

            def isinDanger(self):
             return True

        else:
            print('City is having normal in temperature')
            def isinDanger(self):
                return False

        return tempcity
city1 = City('Jaipur',34)
print(city1.getname(),city1.gettempcity(4))
