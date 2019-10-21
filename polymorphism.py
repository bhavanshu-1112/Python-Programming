# polymorphism
# duck typing
# operator overloading
# mthod overiding

# duck typing
class pycharm:
    def execute(self):
        print('compling')
        print('running')

class myEditor:
    def execute(self):
        print('desiging')
        print('spell check')

class laptop:
    def code(self,ide):
       ide.execute()

p = pycharm()
l1 = laptop()
l1.code(p)
p = myEditor()
l1.code(p)
