import numpy as np
f=open("")
l=[map(float,line.split()) for line in f]
f.close()
n=len(l)
result=[.0]*n
for i in range(n):
	result[i]= ((l[i])[0]+(l[i])[1]+(l[i])[2]+(l[i])[3])/4.

f=open('','w')
for i in range(n):
	f.write("%d\t&\t%.2f&\t%.2f&\t%.2f&\t%.2f&\t%.2f" 
		%((l[i])[0],(l[i])[1],(l[i])[2],(l[i])[3],result[i]))
	f.write("\\\\")
	f.write("\\hline")

f.close()






