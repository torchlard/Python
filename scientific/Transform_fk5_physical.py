
# coding: utf-8

# In[217]:

from __future__ import division
import numpy as np

ra_c=39.969108
dec_c=-1.5787901+0.0000803
resolution=30  #mas
Npix=5600

header=['']*31
f=open('/home/lkit/Data/hlsp_glass_hst_wfc3_a370-fullfov-pa999_ir_v001_redshiftcatalog.txt')
for i in range(31):
    header[i]=(f.readline()).strip()
l=np.asarray([map(float,(line.split())[0:6]) for line in f])
f.close()
f=open('/home/lkit/Data/hlsp_glass_hst_wfc3_a370-fullfov-pa999_ir_v001_redshiftcatalog.txt')
for i in range(31):
    next(f)
comment=np.asarray([map(str,(line.split())[6:]) for line in f])
f.close()

n=len(l)
ra=l[:,1]
dec=l[:,2]+0.0000803
imageX = Npix/2-((ra-ra_c)*60*60*1000/resolution)    #fk5 -> image
imageY = Npix/2+((dec-dec_c)*60*60*1000/resolution)
l[:,1]=imageX; l[:,2]=imageY;

str1= [["%.4f" % x for x in y] for y in l]

str2=[''.join('{0:15}'.format(i) for i in j).strip() for j in str1]
comment2=[' '.join(i) for i in comment]
out=['      '.join(i) for i in np.column_stack((str2,comment2))]

f=open('/home/lkit/Data/Redshift_Catalog_5600scale','w')
for i in range(31):
    f.write(str(header[i]))
    f.write('\n')
np.savetxt(f,out,fmt='%s')
f.close()
print 'finish'

