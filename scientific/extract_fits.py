
# coding: utf-8

# In[68]:

import matplotlib.pyplot as plt
import pyregion

region_name = "/home/lkit/tmp/ds9.reg"
r = pyregion.open(region_name)

x1= 2571
x2= 2633
y1= 3051
y2= 3144

mask_1or2 = r.get_mask(shape=(5600,5600))
myfilter = r.get_filter()
mask_1and2 = ((myfilter[0] &  myfilter[1])).mask((5600,5600))

xor=mask_1or2[y1-1:y2,x1-1:x2]
xand=mask_1and2[y1-1:y2,x1-1:x2]

xor=xor.flatten()
xand=xand.flatten()
print (x2-x1+1)*(y2-y1+1)
print len(xor)

match=[]
for i in range(len(xor)):
    if xand[i]==xor[i]:
        match.append(False)
    else:
        match.append(True)
match=np.asarray(match)
match=np.reshape(match,(y2-y1+1,x2-x1+1))
xand=np.reshape(xand,(y2-y1+1,x2-x1+1))
xor=np.reshape(xor,(y2-y1+1,x2-x1+1))
print match

plt.subplot(121).imshow(xor, origin="lower", interpolation="nearest")
#plt.subplot(122).imshow(xand, origin="lower", interpolation="nearest")
plt.subplot(122).imshow(match, origin="lower", interpolation="nearest")
plt.show()


# In[71]:

f=fits.open('/home/lkit/Data/Jan_data/30mas_v0.5_f435w.fits')
raw=np.asarray(f[0].data)
f.close()
newd=raw[y1-1:y2,x1-1:x2]*46260.

value= []
for i in range(x2-x1+1):     #extract value within annulus
    for j in range(y2-y1+1):
            if (match[j,i]):
                value.append(newd[j,i])
print value


# In[72]:

from scipy.optimize import leastsq
import matplotlib.mlab
import numpy as np
from pylab import *

fig = plt.figure()
#ax = fig.gca(projection='2d')
n,bins,patches=plt.hist(value, bins=50, histtype='stepfilled',align='mid') #define range
#plt.show()
#print 'n,bins,patches= ',n,bins,patches
n_bins=[0]*(len(bins)-1)
for i in range(0,len(bins)-1):
    n_bins[i]=(bins[i]+bins[i+1])/2.
    
mean = sum(n)/len(n)      
su=0
for i in range(0,len(n)):
    su=su+ n[i]*((n_bins[i]-mean)**2)/len(n)      #sigma=sqrt(sum[(x_i-mean)^2]/N)
sigma = np.sqrt(su)
#print sigma  
x=n_bins
y=n
y_proc = np.copy(y)

def gaussian(parms,x):
    c1, mu1, sigma1=parms
    res = c1 * np.exp( - (x - mu1)**2.0 / (2.0 * pow(sigma1,2.0))) 
    return res

def gaussian_fit(parms,x):
    c1, mu1, sigma1=parms
    fit = c1 * np.exp( - (x - mu1)**2.0 / (2.0 * pow(sigma1,2.0))) 
    return (fit - y_proc)

# Least squares fit. Starting values found by inspection.
fit = leastsq( gaussian_fit,[3,100,40],args=(x) )
#plot( x, y, c='b' )
aa,bb,cc=fit[0]
print 'c1,mu1,sigma1= ',fit[0]
# #plot( x, double_gaussian( x, fit[0] ), c='r' )
plot( x, gaussian([aa,bb,cc],x), c='r' )

plt.show()

