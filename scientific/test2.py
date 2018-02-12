from sklearn import mixture
import matplotlib.pyplot as plt
import matplotlib.mlab
import numpy as np
from pylab import *
from scipy.optimize import leastsq

data = np.genfromtxt('/home/lkit/Programming/Python/gaussian_fit.dat', skiprows = 1)
x = data[:, 0]
y = data[:, 1]


def double_gaussian( x, params ):
    c1, mu1, sigma1, c2, mu2, sigma2 = params
    res =   c1 * np.exp( - (x - mu1)**2.0 / (2.0 * sigma1**2.0) ) \
          + c2 * np.exp( - (x - mu2)**2.0 / (2.0 * sigma2**2.0) )
    return res

def double_gaussian_fit( params ):
    fit = double_gaussian( x, params )
    return (fit - y_proc)

# Remove background.
y_proc = np.copy(y)
#y_proc[y_proc < 5] = 0.0

# Least squares fit. Starting values found by inspection.
fit = leastsq( double_gaussian_fit, [13.0,-13.0,1.0,60.0,3.0,1.0] )	#amplitude,mean,sigma
print "fits= ",fit
plot( x, y, c='b' )
plot( x, double_gaussian( x, fit[0] ), c='r' )
plt.show()

fits=  (array([  8.44224554, -13.06037424,   6.54449334,  63.3488999 ,
         2.974897  ,   1.83904606]), 1)















