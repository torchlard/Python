
# coding: utf-8

# In[42]:

from __future__ import division
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
error=[]
# pix2rad = (0.04666/1400.0)*(3.1415927/180.0)
for flag in range(126):
    f_name='/home/lkit/wslap/data/A370/reconstruction/tmp/Beta_vector_VER'+str(flag+1)+'.dat'
    f=open(f_name)
    data=np.asarray([map(float,line.split()) for line in f])
    f.close()
    tmp=[]; final=[]
    for index in set(data[:,1]):
        for j in range(len(data)):
            if (data[j,1]==index):
                tmp.append([data[j,2],data[j,3]])
        final.append(tmp)
        tmp=[]
    final=np.asarray(final)
    fix=[]; fiy=[]
#     print final
    for i in final:
        co=0; tmpx=0; tmpy=0
        for j in i:
            tmpx=tmpx+j[0]
            tmpy=tmpy+j[1]
            co+=1
        fix.append(tmpx/co)
        fiy.append(tmpy/co)
#     print 'fix=',fix
#     print 'fiy=',fiy
    disp=[]; index=0; 
    for i in final:
        dist=0; 
        for j in i:
            dist=dist+sqrt((j[0]-fix[index])**2+(j[1]-fiy[index])**2)
        index+=1
        disp.append(dist)
    error.append(sum(disp))
print error
plt.hist(error,range=[0,300],bins=100)
plt.show()

