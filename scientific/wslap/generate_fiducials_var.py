from __future__ import division
import numpy as np
from Progress import progress_bar as pbr

f=open("/home/lkit/wslap/data/A370/fiducial/1400scale_v10/xy_mass.dat")
data=np.asarray([map(float,line.split()) for line in f])
f.close()

obj=dict(
a=[2632,3258,245,17.5],
b=[2920,3166,299.0389,16.49],
c=[2669,3087,41.757,13.839])
d=[2782,2999,27.35,9.914]

coor=np.asarray([[j/4-700 for j in (obj[i])[:2]] for i in obj.keys()])

min_ver=158
max_ver=163

for ver in range(min_ver,max_ver+1):
    f=open("/home/lkit/wslap/data/A370/fiducial/xy_mass_VER"+str(ver)+".dat",'w')

    scale1 = 100*(1+ver*20)
    scale2 = 0.1*(10+ver*1)
    mass=np.asarray([((obj[i])[2])/scale1 for i in obj.keys()])
    radius=np.asarray([((obj[i])[3])/scale2 for i in obj.keys()])
    for i in data[0]:
        f.write("\t%d\n" %(i+len(obj)))
    for i in data[1:]:
        f.write("%4d\t%4d\t%f\t%f\t0.05\t0\t0\t0\t%d\n" %(i[0],i[1],i[2],i[3],i[8]))
    for r in range(3):
        f.write("%4d\t%4d\t%f\t%f\t0.05\t0\t0\t0\t1\n" %(coor[r,0],coor[r,1],mass[r],radius[r]))

    f.close()

    pbr.printProgress(ver-min_ver,max_ver-min_ver,prefix='Progress:',barLength=100)
