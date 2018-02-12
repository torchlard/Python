
# coding: utf-8

# In[23]:

import numpy as np
f=open('/home/lkit/Data/Source_Catalog_5600scale')
for i in range(21):
    next(f)
l=np.asarray([map(float,line.split()) for line in f])
f.close()
n=len(l)
ra=l[:,1]
dec=l[:,2]     #+0.0000803
flux_auto=l[:,23]
mag_auto=l[:,25]

s1='global color=red'
s2='image'
f=open('/home/lkit/Ds9_regions/GLASS/source_catalog_5600scale.reg','w')
f.write(s1); f.write('\n')
f.write(s2); f.write('\n')
for i in range(n):
    f.write('text\t%f\t%f\t{%.4f}\n' %(ra[i],dec[i],flux_auto[i]))
f.close()
print 'finish'


# In[26]:

f=open('/home/lkit/Data/GlassGigCataog_5600scale')
for i in range(37):
    next(f)
l=np.asarray([map(float,line.split()) for line in f])
f.close()
n=len(l)
ra=l[:,1]; dec=l[:,2]+0.0000803
mag=l[:,5]

s1='global color=red'
s2='image'
f=open('/home/lkit/Ds9_regions/GLASS/Glass_gig_catalog_5600scale.reg','w')
f.write(s1); f.write('\n')
f.write(s2); f.write('\n')
for i in range(n):
    f.write('text\t%f\t%f\t{%.4f}\n' %(ra[i],dec[i],mag[i]))
f.close()
print 'finish'


# In[27]:

f=open('/home/lkit/Data/Redshift_Catalog_5600scale')
for i in range(31):
    next(f)
l=np.asarray([map(float,(line.split())[0:6]) for line in f])
l=np.asarray(filter(lambda x: x[3]!=-1, l))
f.close()
n=len(l)
ra=l[:,1]; dec=l[:,2]+0.0000803;  redshift=l[:,3]; quailty=l[:,4]

# ra1=[]; ra2=[]; ra3=[]; ra4=[];
# dec1=[]; dec2=[]; dec3=[]; dec4=[];
# z1=[]; z2=[]; z3=[]; z4=[];

# for i in range(n):
#     if quailty[i]>=1:
#         ra1.append(ra[i]); dec1.append(dec[i]); z1.append(redshift[i])
#     if quailty[i]>=2:
#         ra2.append(ra[i]); dec2.append(dec[i]); z2.append(redshift[i])
#     if quailty[i]>=3:
#         ra3.append(ra[i]); dec3.append(dec[i]); z3.append(redshift[i])
#     if quailty[i]>=4:
#         ra4.append(ra[i]); dec4.append(dec[i]); z4.append(redshift[i])
        
s1='global color=red'
s2='image'
# f=open('/home/lkit/Ds9_regions/GLASS/Redshift_catalog_q>=1.reg','w')
# f.write(s1); f.write('\n')
# f.write(s2); f.write('\n')
# for i in range(n):
#     f.write('text\t%f\t%f\t{%.4f}\n' %(ra1[i],dec1[i],z1[i]))
# f.close()
# f=open('/home/lkit/Ds9_regions/GLASS/Redshift_catalog_q>=2.reg','w')
# f.write(s1); f.write('\n')
# f.write(s2); f.write('\n')
# for i in range(len(ra2)):
#     f.write('text\t%f\t%f\t{%.4f}\n' %(ra2[i],dec2[i],z2[i]))
# f.close()
# f=open('/home/lkit/Ds9_regions/GLASS/Redshift_catalog_q>=3.reg','w')
# f.write(s1); f.write('\n')
# f.write(s2); f.write('\n')
# for i in range(len(ra3)):
#     f.write('text\t%f\t%f\t{%.4f}\n' %(ra3[i],dec3[i],z3[i]))
# f.close()
# f=open('/home/lkit/Ds9_regions/GLASS/Redshift_catalog_q>=4.reg','w')
# f.write(s1); f.write('\n')
# f.write(s2); f.write('\n')
# for i in range(len(ra4)):
#     f.write('text\t%f\t%f\t{%.4f}\n' %(ra4[i],dec4[i],z4[i]))
# f.close()
f=open('/home/lkit/Ds9_regions/GLASS/Redshift_catalog_color_5600scale.reg','w')
f.write(s1); f.write('\n')
f.write(s2); f.write('\n')
for i in range(n):
    if quailty[i]==1:
        f.write('text\t%f\t%f\t{%.3f} # color=magenta\n' %(ra[i],dec[i],redshift[i]))
    if quailty[i]==2:
        f.write('text\t%f\t%f\t{%.3f} # color=cyan\n' %(ra[i],dec[i],redshift[i]))
    if quailty[i]==2.5:
        f.write('text\t%f\t%f\t{%.3f} # color=cyan\n' %(ra[i],dec[i],redshift[i]))
    if quailty[i]==3:
        f.write('text\t%f\t%f\t{%.3f} # color=green\n' %(ra[i],dec[i],redshift[i]))
    if quailty[i]==3.5:
        f.write('text\t%f\t%f\t{%.3f} # color=green\n' %(ra[i],dec[i],redshift[i]))
    if quailty[i]==4:
        f.write('text\t%f\t%f\t{%.3f} # color=red\n' %(ra[i],dec[i],redshift[i]))
f.close()
print 'finish'


# In[13]:

from matplotlib import pyplot as plt
plt.hist(ra3,bins=70)#0,range=(0.35,0.4))
plt.xlabel('redshift')
plt.ylabel('frequency')
plt.show()


# In[94]:

core=np.asarray(filter(lambda x: (x[3]<=0.5 and x[3]>=0.3) , l))
ra=core[:,1]; dec=core[:,2]+0.0000803;  redshift=core[:,3]
n=len(core)
s1='global color=red'
s2='fk5'
f=open('/home/lkit/Ds9_regions/GLASS/core_z.reg','w')
f.write(s1); f.write('\n')
f.write(s2); f.write('\n')
for i in range(n):
    f.write('text\t%f\t%f\t{%.4f}\n' %(ra[i],dec[i],redshift[i]))
f.close()

f=open('/home/lkit/Ds9_regions/GLASS/member_indication.reg','w')
f.write(s1); f.write('\n')
f.write(s2); f.write('\n')
for i in range(n):
    f.write('boxcircle point %f %f\n' %(ra[i],dec[i]))
f.close()
print 'finish'


# In[ ]:



