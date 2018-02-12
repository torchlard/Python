from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import math

obj = Series([4,7,-5,3])
obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
print(obj2[['d','c']])
print(np.exp(obj2))

# %% build series

sdata = {'Ohio': 35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
states = ['Cali','Ohio','Oregon','Texas']
obj3 = Series(sdata, index=states)

print(pd.notnull(obj3))

# %% build dataframe

data = {'state': ['ohio','ohio','ohio','nevada','nevada'],
        'year': [2000,2001,2002,2001,2002],
        'pop': [1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data, columns=['year','state','pop','debt'],
                        index=['one','two','three','four','five'])

frame['debt'] = np.arange(1.,6.)
# print(frame.columns)
# print(frame.loc['three'])

# add column
frame['eastern'] = frame.state == 'ohio'
# del column
del frame['year']
print(frame)

# %% convert from data frame to numpy
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
x = frame3.values
type(x[0])

# %% reindex, fill gaps
states = ['Texas','Utah','California']
obj3 = Series(['blue','purple','yellow','brown'], index=[0,2,4,9])
obj3 = obj3.reindex(range(12), method='ffill')
# print(obj3)

frame = DataFrame(np.arange(9).reshape((3,3)), index=['a','c','d'],
    columns=['Ohio','Texas','California'])
frame2 = frame.reindex(['a','b','c','d'], method='bfill')
frame3 = frame.loc[['a','b','c','d'], states]
print(frame)
print(frame2)
print(frame3)

# drop entries
frame3 = frame3.drop(['b','c'])
print(frame3)
frame3 = frame3.reindex(columns=['California','Texas','r'])
print(frame3)
frame3 = frame3.drop(['Texas'], axis=1)
print(frame3)

# %% filter series
obj = Series(np.arange(1.,5.), index=['a','b','c','d'])
print(obj)
print(obj['b':'d'])
print(obj[2:4])
print(obj[obj<3])

# %% filter DataFrame
data = DataFrame(np.arange(16).reshape((4,4)), index=['ohio','new york','utah','corol'],
    columns=['one','two','three','four'])
print(data)
print(data[2:3])
print(data[['one','three']])
print(data[data['three']>6])
# data[data<5] = 0
# print(data)
print(data.loc[['new york','corol'],['two','three']] )

# %% Arithmetic
s1 = Series([-7.3,-2.5,3.4, 1.5], index=list('acde'))
s2 = Series([-2.1,3.6,-1.5,4,3.1], index=list('acefg'))
print(s1)
print(s2)
print(s1+s2)
print(s1.add(s2, fill_value=0))

# %% functions
frame = DataFrame(np.random.randn(4,3), columns=list('bde'),
    index=['utah','ohio','texas','oregon'])
print(frame)
np.abs(frame)
f = lambda x: x.max()-x.min()
frame.apply(f, axis=0)
frame.apply(f, axis=1)
def g(x):
    return Series([x.min(),x.max()], index=['min','max'])
frame.apply(g)
format = lambda x: "%.2f" %x
frame.applymap(format)
frame.sum(axis=1)
frame.describe()

# %% hierarchical indexing
data = Series(np.random.randn(10),index=[list('aaabbbccdd'),[1,2,3,1,2,3,1,2,2,3]])
print(data)
data['b']
data[5]
data.unstack()

# %% join and merge
from IPython.display import display, HTML
raw_data = {
    'subject_id': ['1','2','3','4','5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}
df_a = pd.DataFrame(raw_data)
display(df_a)
raw_data = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}
df_b = pd.DataFrame(raw_data)
display(df_b)
raw_data = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}
df_n = pd.DataFrame(raw_data)
display(df_n)
pd.concat([df_a,df_b])
pd.concat([df_a, df_b], axis=1)
pd.merge(df_b, df_a, on='subject_id')
pd.merge(df_b, df_n, on='subject_id', how='outer')

