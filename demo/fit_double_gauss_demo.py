import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

######################################
# Setting up test data
def norm(x, mean, sd):	#sd=sigma=std1,std2
  norm = []
  for i in range(x.size):
    norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - mean)**2/(2*sd**2))]	#gauss formula
  return np.array(norm)

mean1, mean2 = 0, -2
std1, std2 = 0.5, 1 

x = np.linspace(-20, 20, 500)
y_real = norm(x, mean1, std1) + norm(x, mean2, std2)

######################################
# Solving
m, dm, sd1, sd2 = [5, 10, 1, 1]
p = [m, dm, sd1, sd2] # Initial guesses for leastsq
y_init = norm(x, m, sd1) + norm(x, m + dm, sd2) # For final comparison plot

def res(p, y, x):
  m, dm, sd1, sd2 = p	#read values from vector p
  m1 = m
  m2 = m1 + dm
  y_fit = norm(x, m1, sd1) + norm(x, m2, sd2)
  err = y - y_fit
  return err

plsq = leastsq(res, p, args = (y_real, x))

y_est = norm(x, plsq[0][0], plsq[0][2]) + norm(x, plsq[0][0] + plsq[0][1], plsq[0][3])

plt.plot(x, y_real, label='Real Data')
plt.plot(x, y_init, 'r.', label='Starting Guess')
plt.plot(x, y_est, 'g.', label='Fitted')
plt.legend()
plt.show()
