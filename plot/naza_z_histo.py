#fitting redshift of objects in nasa catalog 

import numpy as np
import matplotlib.pyplot as plt
import math
from math import exp 
import statistics as st
from scipy.optimize import curve_fit


def z_to_v(Max_z):

 PI = 3.1415927
 Omega  = 0.3
 Lambda = 0.7
 DH     = 3000.0/0.7  #units of h^-1   DH = 3000/h, h=0.7
 N_z    = 10000
 incr_z = Max_z/float(N_z)
 z_int  = 0.0
 Dc     = 0.0
 for i_z in range (1,N_z):
         z_int = z_int + incr_z
         E_z=math.sqrt((((1.0+z_int)**3)*Omega) + Lambda)
         Dc = Dc + DH*incr_z/E_z

 v=Dc*70

 return v;
##############################################################

data=[0]*179
f=open('/home/lkit/Data/2015Dec_ref/nasa_z.dat')
i=0
for line in f:
 data[i]=float(line)
 i+=1
f.close()

diff_z= [0]*179
for i in range (0,178): 
 diff_z[i]=z_to_v(Max_z=data[i])-z_to_v(Max_z=0.373189359903)

sel=diff_z
print 'overall distributions'
print 'max= ', max(sel)
print 'min= ', min(sel)
print 'width= ', max(sel)-min(sel)
print 'SD= ', st.stdev(sel)
print 'mean= ', st.mean(sel)
print 'len_sel= ',len(sel)

n,bins,patches=plt.hist(sel, bins=70, range=(-5000,5000), histtype='stepfilled',align='mid') #define range
#plt.show()

n_bins=[0]*(len(bins)-1)
for i in range(0,len(bins)-1):
 n_bins[i]=(bins[i]+bins[i+1])/2.

#print n,n_bins,patches
#print "n= ",len(n)
#print "n_bins= ",len(n_bins)
#print "patches=",len(patches)
                  
mean = sum(n)/len(n)      
su=0
for i in range(0,len(n)):
 su=su+ n[i]*((n_bins[i]-mean)**2)/len(n)		#sigma=sqrt(sum[(x_i-mean)^2]/N)
sigma = np.sqrt(su)				 #must use np. :P

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2));

print "sigma= ",sigma

x=n_bins
y=n
popt,pcov = curve_fit(gaus,x,y,p0=[1,mean,sigma])

print n

plt.plot(x,gaus(x,*popt),'ro:',label='fit')
plt.legend()
plt.xlabel('km/s velocity')
plt.ylabel('counts')

plt.show()













