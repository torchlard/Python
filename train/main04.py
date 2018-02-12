from collections import namedtuple

Duck = namedtuple('Duck','bill tail')
duck = Duck('aa','bb')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {"bill":"man", "tail":"page"}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnify', bill="glass")
print(duck3)
