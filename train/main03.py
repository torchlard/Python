class testDec():
    count = 0  # shared across class instance
    def __init__(self, value, words="Amy"):
        print ('We are in __init__')
        self.x = value # Will call the setter. Note just x here
        self.words = words
        testDec.count += 1
    @property
    def x(self):
        print ('called getter')
        return self._x+3 # Note the _x here
    @x.setter
    def x(self, value):
        print ('called setter')
        self._x = value+1 # Note the _x here
    def exclaim(self):
        print("I am A")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")
    @staticmethod # no self/class needed
    def commercial():
        print("this coyoteWeapon bring you to Alice")
    def says(self):
        return self.words+'.'

class Quote1(testDec):
    def says(self):
        return self.words+'?'

class Quote2(Quote1):
    def says(self):
        return self.words+'!'

t = testDec(19)
print( t.x)

t2 = testDec(20)
t3 = testDec(20)
testDec.kids()

testDec.commercial()

obj1 = Quote1(11)
print(obj1.says())

# %%

data = {'name':'Hydrogen', 'symbol':'H','number':'1'}

class Element():
    def __init__(self, obj):
        self.name = obj['name']
        self.symbol = obj['symbol']
        self.number = obj['number']
    def __str__(self):
        return self.name+' '+self.symbol+' '+self.number
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,x):
        self._name = x
    @property
    def symbol(self):
        return self._symbol
    @symbol.setter
    def symbol(self,x):
        self._symbol = x
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self,x):
        self._number = x

a = Element(data)
print(a)

# %%

class Laser():
    def does(self):
        return "'distintegrate'(Laser)"

class Claw():
    def does(self):
        return "'crush'(Claw)"

class SmartPhone():
    def does(self):
        return "'ring'(SmartPhone)"

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())

a= Robot()
a.does()
