items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
less = list(filter(lambda x: x<2, items))
product = reduce( (lambda x,y: x+y), [1,2,3] )

square2 = [i**2 for i in items]
less2 = [i for i in items if i<2]

print(squared)
print(square2)
print(less)
print(less2)
print(product)



