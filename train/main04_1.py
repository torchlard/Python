def generator_function():
    for i in range(3):
        yield i

def fibon(n):
    a = b =1
    for i in range(n):
        yield a
        a,b = b,a+b

gen = generator_function()

my_Str = "Yassob dfad"
my_iter = iter(my_Str)
count=0
for i in my_iter:
    if (i=="a"):
        count+=1
print(count)
