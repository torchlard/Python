class Vehicle():
    def __init__(self):
        print("drive car")

def decor(func):
    def do(*args, **kwargs):
        print("inside printer")
        func(*args, **kwargs)
    return do

class Car(Vehicle):
    def __init__(self,name):
        super().__init__()
        self.name = name
    @decor
    def printName(self):
        print(self.name)
    # def get_name(self):
    #     print('inside getter')
    #     return self.name
    # def set_name(self, input):
    #     print('inside setter')
    #     self.name = input
    # pro = property(get_name, set_name)

aa = Car("Benz")
aa.printName()


