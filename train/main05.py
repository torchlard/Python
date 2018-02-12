import csv

with open('villains','rt') as fin:
    csvin = csv.DictReader(fin, fieldnames=['first','last'])
    vin = [row for row in csvin ]

print(vin)

# %%

import xml.etree.ElementTree as et
tree = et.ElementTree(file="menu.xml")
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag: ',child.tag, 'attributes: ',child.attrib)
    for gradnchild in child:
        print("\ttag: ",gradnchild.tag, 'attrib: ',gradnchild.attrib)

# %%
import pickle

class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
str(obj1)
# turn obj1 to pickled binary string
pickled = pickle.dumps(obj1)
print(pickled)
obj2 = pickle.loads(pickled)
print(str(obj2))



