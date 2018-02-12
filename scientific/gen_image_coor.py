#generate input files theta vector from regions

import numpy as np

f=open("/home/lkit/wslap/data/A370/image_region_5600scale.dat")
l=[]
l=[map(float,line.split()) for line in f]
f.close()
n=len(l)
scale=5600.
target=1400.
datax1=np.zeros(n)
datay1=np.zeros(n)
datax2=np.zeros(n)
datay2=np.zeros(n)
dataz=np.zeros(n)
dx=np.zeros(n)	#centroid of images 5600 scale
dy=np.zeros(n)   #centroid of images 5600 scale
dx_red=[0]*n
dy_red=[0]*n
for i in range(n):
	datax1[i]=(l[i])[0]
	datax2[i]=(l[i])[1]
	datay1[i]=(l[i])[2]
	datay2[i]=(l[i])[3]
	dx[i]=(datax2[i]+datax1[i])/2.
	dy[i]=(datay2[i]+datay1[i])/2.
	dataz[i]=(l[i])[4]
	dx_red[i]=int(round(dx[i]/scale*target))
	dy_red[i]=int(round(dy[i]/scale*target))
	
f=open('/home/lkit/wslap/data/A370/theta_vector_database.dat','w')
for i in range(n):
	f.write("%.1f\t\t%d\t\t%d\n" %(dataz[i],dx_red[i],dy_red[i]))	
f.close()


'''
#gen regions to verify positions
f=open('/home/lkit/Ds9_regions/tmp/test.reg','w')
f.write("global color=green\n")
f.write("physical\n")
for i in range(n):
	f.write("# text(%d,%d) text={%d}\n" %(dx_red[i],dy_red[i],dataz[i]))
f.close()
'''


