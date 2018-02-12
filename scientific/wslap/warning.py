import sys
import numpy as np
import itertools

x=[]; filt=[]
arg=sys.argv
i=1
while (arg[i] != 'n'):
	x.append(arg[i])
	i+=1
i+=1
while (arg[i] != 'n'):
	filt.append(float(arg[i]))
	i+=1
print arg[-1]
if (arg[-1] != 'n'): z=int(arg[-1])


f=open('/home/lkit/wslap/data/A370/theta_vector_database.dat')	#database of image coors
vec=[]
vec=[map(float,line.split()) for line in f]
f.close()

print 'filt= ',filt

n1=len(vec)
testing=[]	#changing images
filt_no=[]

for i in range(n1):
	if x:
		for yy in x:
			if int((vec[i])[0]) == int(yy): testing.append(float((vec[i])[0]));
if filt:
	for i in range(len(filt)):
		for j in range(len(testing)):
			if testing[j] == filt[i]: 
				filt_no.append(j);
	filt_no=set(filt_no)
	n_filt=len(filt_no)

comb=[]
stuff = range(len(testing))
if testing:
	for L in range(0, len(stuff)+1):
		for subset in itertools.combinations(stuff, L):
			if filt:
				n=len(filt_no&set(subset))
				if n==n_filt or n==0:
					comb.append((subset))
			else:
				comb.append((subset))
	del comb[0];

#######
print comb



#######3

if not testing: comb=[(0)];
n2=len(comb)
if (arg[-1] != 'n'): n2=n2*z
hour=int(n2*65/60./60.)
minut=n2*65/60.-60*hour
print "There will be %d iterations. Total time required: %d hours %.1f minutes\n" %(n2,hour,minut)
