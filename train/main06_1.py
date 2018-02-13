def hi(name="yasoo"):
    # print("now in hi()")
    def greet():
        return "now in greet()"
    def welcome():
        return "now in welcome"
    if name == "yasoo":
        return greet
    else:
        return welcome
    
a = hi()
print( a() )

# %%

def come(str):
    def wrapFunction():
        print( "I come now, hey "+str)
    return wrapFunction
    
def doSthBefore(func):
    print ("I will do sth before come")
    (func("Tom"))()
    
doSthBefore(come)

# %%

from functools import wraps
def monster(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "function will not run"
        return f(*args, **kwargs) # return original function
    return decorated # unchanged

@monster
def func():
    return ("Function is running")

can_run = True
print(func())
can_run = False
print(func())

# %%









