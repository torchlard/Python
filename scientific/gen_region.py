import numpy as np

# generate ds9 physical region from xy_nasa & corrected_offset

f=open("/home/lkit/ds9_regions/xy_nasa.reg")
l=[]
l=[map(float,line.split()) for line in f]
f.close()
n=len(l)
datax=np.zeros(n)
datay=np.zeros(n)
for i in range(n):
    datax[i]=(l[i])[0]
    datay[i]=(l[i])[1]

f=open('/home/lkit/gg.reg','w')
f.write('global color=red\n')
f.write('physical\n')
for i in range(n):
    s="boxcircle point %.4f %.4f\n" %(datax[i],datay[i])
    f.write(s)
f.close()

f=open("/home/lkit/ds9_regions/correct_offset_nasa.reg")
l=[]
l=[map(float,line.split()) for line in f]
f.close()
n=len(l)
datax=np.zeros(n)
datay=np.zeros(n)
for i in range(n):
    datax[i]=(l[i])[0]
    datay[i]=(l[i])[1]

f=open('/home/lkit/corrected.reg','w')
f.write('global color=green\n')
f.write('physical\n')
for i in range(n):
    s="boxcircle point %.4f %.4f\n" %(datax[i],datay[i])
    f.write(s)
f.close()

