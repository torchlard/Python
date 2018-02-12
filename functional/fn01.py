from fn.func import curried
from functools import reduce
import random
from collections import namedtuple


# ans = ['a','b','c','d','e']
# quiz = [('a',1),('c',2),('d',3),('d',4),('k',5)]
#
# reduced = reduce(lambda x, y: x + y[1][1], filter(lambda x: x[0] == x[1][0], zip(ans, quiz)), 1)
# print (reduced)
#
# price = [1,2,3,4]
# print( reduce(lambda x,y: x*y, [1,2,3,4]) )
#
# print (list(map(lambda x: x, [1,2,3,4])))

bigmuls = lambda xs,ys: filter(lambda x,y:x*y > 25, combine(xs,ys))
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
data = bigmuls([1,2,3,4],[10,15,3,22])

# [(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]
