from __future__ import division	
import matplotlib.pyplot as plt
import numpy as np
import math
import re
#Module 're' provides regular expression matching operations similar to those found in Perl. Both patterns and strings to be searched can be Unicode strings as well as 8-bit strings.
#Eg. m = re.search('(?<=abc)def', 'abcdef')
#    m.group(0) 	>> 'def'
from scipy.optimize import curve_fit
import operator
#The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y. The function names are those used for special class methods; variants without leading and trailing __ are also provided for convenience.
		
#In the future, Python will switch to always yielding a real result,
# and to force an integer division operation you use the special "//"
# integer division operator.  If you want that behavior now, just
# import that "from the future:from __future__ import division
# now: 1 / 2 --> 0.5, 4 / 2 --> 2.0
#      1 // 2 --> 0, 4 // 2 --> 2
import itertools
import pyfits

#critcurve_dir = '/Volumes/BRIAN/Research/WSLAP_works/data/M0647/ver21/reconstruction/critcurve_map_ver21_full.fits'
m_zp = 24.6949		#magnitude zero oint
gain = 2		# check from header
t =  79744.0 #integration time (second)

image_parameters_dir = '/home/lkit/Data/image_parameters.dat'

f = file(image_parameters_dir)
next(f) 				#skip the first line (header line)
parms = np.empty(12)
for line in f:
    line = line.strip()  #remove the \n at the end of line
    T = line.split("\t")  #split according to 
    T = np.asarray(T)     #change list to array
    parms = np.vstack((parms, T))
parms = np.delete(parms, (0), axis=0)  #delete the first row (0,0,0...)
parms = parms.astype(np.float) 
#print parms
def f7(seq):			
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

key=[int (x) for x in f7(map(lambda x:x[0],parms))]   #generate reference key: by source number
parms=np.column_stack((parms,key))   #stack reference key to end of each line

values=set(map(lambda x:x[12],parms))
objID=[[y[0] for y in parms if y[12]==x] for x in values]
adu=[[y[9] for y in parms if y[12]==x] for x in values]
sigma=[[y[10] for y in parms if y[12]==x] for x in values]
Area=[[y[8] for y in parms if y[12]==x] for x in values]
mu=[[y[11] for y in parms if y[12]==x] for x in values]




#================================================================== 
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Functions for basic mathematical operations
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 

def PLUS(L1,L2):
    return [map(operator.add,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def plus(L1,n):
    return [[x + n for x in obj] for obj in L1]

def MINUS(L1,L2):
    return [map(operator.sub,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def minus(L1,n):
    return [[x - n for x in obj] for obj in L1]

def MULTIPLY(L1,L2):
    return [map(operator.mul,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def multiply(L1,n):
    return [[x * n for x in obj] for obj in L1]

def DIVIDE(L1,L2):
    return [map(operator.truediv,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def divide(L1,n):
    return [[x / n for x in obj] for obj in L1]

def square(L1):
    return [[x ** 2 for x in obj] for obj in L1]

def squareroot(L1):
    return [[x ** 0.5 for x in obj] for obj in L1]

def openup(L): # accept a list with tuple, return with a list without tuple
    temp = []
    for sys in L:
        temp = temp + list(sys)
    return np.asarray(temp)

# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Scientific Functions
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 

def magnitude(flux):  # return the magnitude correspond to the flux, input number only
    M = -2.5*(np.log10(flux)) + m_zp
    return M

def MAGNITUDE(flux):  # operate on whole list: [[],[],[]]
    return [[magnitude(x) for x in obj] for obj in flux]

def dM(flux, df):  # return the magnitude error based on flux and fluxErr, input number only
    err = 1.0851/flux * df
    return err

def DM(flux, df):  #operate on the whole list: [[],[],[]]
    return [map(dM,flux[flux.index(obj)],df[flux.index(obj)]) for obj in flux]



#================================================================== 

# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Obtain the total error (ADUs^-1) from the wht image and object flux
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 

OBJ1 = divide(adu, gain * t)
OBJ2 = MULTIPLY(square(Area),square(sigma))

NOISE = squareroot(PLUS(OBJ1,OBJ2))
#print(NOISE)
#================================================================== 


# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Get an array of object's magnitude and magnitude error
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
lum = multiply(adu, gain)  #change the total image flux to e-s^-1 unit
lumErr = multiply(NOISE, gain)  #change the total error to e-s^-1 unit

mag = MAGNITUDE(lum)  #change the luminosity list into magnitude
magErr = DM(lum,lumErr)  #change the lumErr list to magnitude error

print(' The magnitudes of sources are: ' + str(mag))
print(' The magnitudes error of sources are: ' + str(magErr))

# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Functions to arrange the elements in appropriate form for plotting graph 1
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 

def duplicate(data):  #rearrange the data, applicable to observeded magnitude, observed magnitude error
    #[['1a', '1b', '1c'], ['2a', '2b'] -> [1a, 1a, 1b, 1b, 1c, 1c, 2a, 2b]
    v = []
    for system in data:
        for value in system:
            for i in range(len(system)-1):
                v.append(value)
    return np.asarray(v)

def perm(data):  #rearrange the data, applicable to perdicted magnitude, predicted magnitude error
    #[['1a', '1b', '1c'], ['2a', '2b'] -> [1b, 1c, 1a, 1c, 1a, 1b, 2b, 2a]
    result = []
    for sys in data:
        temp = [np.concatenate((sys[:i],sys[i+1:])) for i in range(len(sys))]
        temp = np.array(temp).flatten()
        result = np.concatenate((result, temp))
    return result
    
def predicted(flux0, mu):  # predicted magnitude (order in perm(data))
    array_flux0 = perm(flux0)
    array_M0 = magnitude(array_flux0)
    array_mu0 = perm(mu)
    array_muI = duplicate(mu)
    predMag = array_M0 + 2.5*(np.log10(array_mu0/array_muI))
    return predMag

# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Construct the x and y axis for the plot 1
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
x = duplicate(mag)
y = map(operator.sub,predicted(lum,mu),duplicate(mag))
yErr = map(operator.add,perm(magErr),duplicate(magErr))

#plot the graph
plt.errorbar(x, y, yerr = yErr, fmt='o')
#plt.axis([17, 29, 17, 29])
plt.xlabel('Observed Magnitude')
plt.ylabel('Predicted Magnitude - Observed Magnitude')
#plt.plot(range(100),range(100))
#plt.plot(fit_x, fit_y, 'r')
plt.show()


#================================================================== 
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Functions to align data in plot 2
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# Consider we have a data: L = [['1a','1b','1c'],['2a','2b','2c']],
# We make combinations of all elements inside the inner bracket, and store the elemnt separately into two arrays
# arrayI(L) = ['1b','1c','1c','2b','2c','2c']
# arrayO(L) = ['1a','1a','1b','2a','2a','2b']
def arrayI(L):
    I = []
    for sys in L:
        for C in itertools.combinations(sys,2):
            (itemO,itemI) = C
            I.append(itemI)
    return I

def arrayO(L):
    O = []
    for sys in L:
        for C in itertools.combinations(sys,2):
            (itemO,itemI) = C
            O.append(itemO)
    return O

# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Construct the x and y axis for the plot 2
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
M_O = arrayO(mag)
M_I = arrayI(mag)
mu_O = arrayO(mu)
mu_I = arrayI(mu)
MErr_O = arrayO(magErr)
MErr_I = arrayI(magErr)

x_int = map(operator.truediv,mu_I,mu_O)
x = [-2.5 * np.log10(i) for i in x_int]
y = map(operator.sub, M_I, M_O)
yErr = map(operator.add,MErr_O,MErr_I)

plt.errorbar(x, y, yerr = yErr, fmt='o')

#calculate and plot best fit line

def fit_func(x, a, b):
    return a*x + b

params = curve_fit(fit_func, x, y)

[a, b] = params[0]

fit_x = np.arange(-7, 7)
fit_y = a*fit_x + b
plt.plot(fit_x, fit_y, 'r')
print(a)
print(b)

#plot a reference 1 to 1 line
x_ref = np.arange(-7,7)
y_ref = np.arange(-7,7)
plt.plot(x_ref, y_ref, 'green')
plt.xlabel('-2.5log(mu_p/mu_0)')
plt.ylabel('Predicted Magnitude - Observed Magnitude')
plt.axis([-3, 2, -4, 4])
#np.save.fig('~/figure1.jpeg')
plt.show()


# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
# 
#   Construct the x and y axis for the plot 3 (Daniel's plot)
#   
# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * 
x = duplicate(mag)
xErr = duplicate(magErr)
y = predicted(lum,mu)
yErr = perm(magErr)

plt.errorbar(x, y, xerr = xErr, yerr = yErr, fmt='o')

#calculate and plot best fit line

def fit_func(x, a, b):
    return a*x + b

params = curve_fit(fit_func, x, y)

[a, b] = params[0]

fit_x = np.arange(0, 100)
fit_y = a*fit_x + b
plt.plot(fit_x, fit_y, 'r')

#plot a reference 1 to 1 line
x_ref = np.arange(0,100)
y_ref = np.arange(0,100)
plt.plot(x_ref, y_ref, 'green')

plt.xlabel('Observed Magnitude')
plt.ylabel('Predicted Magnitude')
plt.axis([19, 28, 19, 28])
plt.show()

import itertools

for item in itertools.combinations(['1a','1b','1c'],2):
    (item1,item2) = item
    print(item1)

test = [['1a','1b','1c'],['2a','2b','2c']]
def arrayI(L):
    I = []
    for sys in L:
        for C in itertools.combinations(sys,2):
            (itemO,itemI) = C
            I.append(itemI)
    return I
def arrayO(L):
    O = []
    for sys in L:
        for C in itertools.combinations(sys,2):
            (itemO,itemI) = C
            O.append(itemO)
    return O
print(arrayI(test))
print(arrayO(test))
# In[5]:

#import matplotlib.pyplot as plt
#import numpy as np
#import math
#import re
#from scipy.optimize import curve_fit
#import operator
#from __future__ import division

adu = [       [40.0353,29.4606,19.8437],       [7.70359,9.625452,5.1469589],       [0.893754165102,1.87928501961],       [1,12.0289544153,3.48911362055],       [0.654471534472,0.464703521739],       [1.62446953174,1.71061766302,0.395701680637],       [10.5085617047,5.83603933067,2.48269709371],       [12.0657174981,11.9871428602],       [4.77205282147,0.872451539683,0.875281728573]      ] #total adu included inside the aperture of the object

test1 = [[1,2],[5,55,7],[1,4,0.1]]
test2 = [[8,1],[9,82,109],[0.1,1,4]]


def PLUS(L1,L2):
    return [map(operator.add,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def plus(L1,n):
    return [[x + n for x in obj] for obj in L1]

def MINUS(L1,L2):
    return [map(operator.sub,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def minus(L1,n):
    return [[x - n for x in obj] for obj in L1]

def MULTIPLY(L1,L2):
    return [map(operator.mul,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def multiply(L1,n):
    return [[x * n for x in obj] for obj in L1]

def DIVIDE(L1,L2):
    return [map(operator.truediv,L1[L1.index(obj)],L2[L1.index(obj)]) for obj in L1]

def divide(L1,n):
    return [[x / n for x in obj] for obj in L1]

def square(L1):
    return [[x ** 2 for x in obj] for obj in L1]

def squareroot(L1):
    return [[x ** 0.5 for x in obj] for obj in L1]

def openup(L): # accept a list with tuple, return with a list without tuple
    temp = []
    for sys in L:
        temp = temp + list(sys)
    return np.asarray(temp)

def magnitude(flux):  # return the magnitude correspond to the flux, input number only
    M = -2.5*(np.log10(flux)) + m_zp
    return M

def MAGNITUDE(L):  # whole object
    return [[magnitude(x) for x in obj] for obj in L]


lum = multiply(adu, gain)  #change the total image flux to e-s^-1 unit

print(PLUS(test1,test2))
print(plus(test1,1))
print(MINUS(test1,test2))
print(minus(test1,1))
print(MULTIPLY(test1,test2))
print(multiply(test1,1))
print(DIVIDE(test1,test2))
print(divide(test1,2))
print(magnitude(40))
print(MAGNITUDE(lum))

A = [1,2,3]
print(3*A)




