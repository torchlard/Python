import sys
import numpy as np
import itertools

def f7(seq):			#clear duplicate elements without disturbing order
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
 
arg=sys.argv
x=[]; y=[]; z=[]; filt=[]; i=1
while (arg[i] != 'n'):
	x.append(arg[i])
	i+=1
i+=1
while (arg[i] != 'n'):
	y.append(arg[i])
	i+=1   
i+=1
while (arg[i] != 'n'):
	filt.append(float(arg[i]))
	i+=1        
i+=1
while (arg[i] != 'n'):
	z.append(int(arg[i]))
	i+=1 

N_size=int(arg[-2])  
ver=int(arg[-1])
#print 'z= ',z

if z:
	seq_z=[0.]*z[2]
	value=z[0]
	for z_i in range(z[2]):
		seq_z[z_i]=value
		value+=float(z[1])/z[2]


# print '\nx= ',x
# print '\ny= ',y

f=open('/home/lkit/wslap/data/A370/theta_vector_database.dat')	#database of image coors
vec=[]
vec=[map(float,line.split()) for line in f]
f.close()
f=open('/home/lkit/wslap/data/A370/xy_source_database.dat')	#database of source redshift
source=[]
source=[map(float,line.split()) for line in f]
f.close()

#print vec
#print source

n=len(vec)
stable=[]	#unchange images
testing=[]	#changing images
testing_index=[]
filt_no=[]

for i in range(n):
	if x: 
		for xx in x:
			if int((vec[i])[0]) == int(xx): stable.append(vec[i]);
	if y:
		for yy in y:
			if int((vec[i])[0]) == int(yy): 
				testing.append(vec[i]) 
				testing_index.append(float((vec[i])[0]))
#print 'stable= ',stable
#print 'testing= ',testing

# generate testing combinations
if filt:
	for i in range(len(filt)):
		for j in range(len(testing_index)):
			if testing_index[j] == filt[i]: 
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
if not testing: comb=[(0)];
#print 'comb= ',comb

# create different versions of theta_vector

#for each iteration,real & tmp files are created
if not z:
	for sub in comb:		#sub=blocks of combinations
		#print 'sub= ',sub
		s1= "/home/lkit/wslap/data/A370/observation/tmp/tmp_theta_VER%d" %(ver)
		s2="/home/lkit/wslap/data/A370/observation/real_theta_VER%d" %(ver) 
		s3="/home/lkit/wslap/data/A370/observation/tmp/tmp_source_VER%d" %(ver)
		# s1="/home/lkit/testing_tmp_theta"
		# s2="/home/lkit/aaa"
		# s3="/home/lkit/bbb"
		f1=open(s1,'w')
		f2=open(s2,'w')
		f3=open(s3,'w')
		count=1; level=1; flag=1
		tmp1=[]; tmp2=[];
		if stable: past=int((stable[0])[0]);
		if not stable: past=int((testing[0])[0]);
		#print 'past=',past
		if stable:
			for i in range(len(stable)):
				sys=int((stable[i])[0])			#system number
				if past!=sys: 			# turn system numbers to seq of natural number
					level+=1
					flag=1
				f1.write("%d\t\t%d\t\t%d\t\t%d\t\t%d\n" %(count,level,(stable[i])[1],(stable[i])[2],0))
				count+=1; past=sys  	#set past value to new sys
				f2.write("%.1f\n" %((stable[i])[0]))
				#f2.write("%.1f\t\t%d\t\t%d\n" %((stable[i])[0],(stable[i])[1],(stable[i])[2]))
				if flag==1:
					for ii in range(len(source)):
						if sys==int((source[ii])[0]): 
							tmp1.append(int((source[ii])[0]))		# store source number
							tmp2.append((source[ii])[1]) 			# store redshift value for source
							flag=0
							break; 			
		flag=1
		if testing:
			for j in sub:
				#print 'j= ',j
				sys=int((testing[j])[0])
				if past!=sys: 
					level+=1
					flag=1
				f1.write("%d\t\t%d\t\t%d\t\t%d\t\t%d\n" %(count,level,(testing[j])[1],(testing[j])[2],0))
				f2.write("%.1f\n" %((testing[j])[0]))
				#f2.write("%.1f\t\t%d\t\t%d\n" %((testing[j])[0],(testing[j])[1],(testing[j])[2]))
				count+=1; past=sys  
				if flag==1:
					for ii in range(len(source)):
						#print 'tmp2= ',tmp2 
						if sys==int((source[ii])[0]):
							tmp1.append(int((source[ii])[0]))		#list of image source 
							tmp2.append(float((source[ii])[1])) 	# list of redshift
							flag=0
							break;
		#tmp1=f7(tmp1); tmp2=f7(tmp2)
		f3.write("\t\t%d\n" %len(tmp1))
		#print 'tmp1= ',tmp1
		#print 'tmp2= ',tmp2
		for k in range(len(tmp1)):
			f3.write("\t\t%d\t\t%d\t\t%d\t\t30\t\t%f\t\tsource_1.txt2\n" %(k+1,N_size/2,N_size/2,tmp2[k]))   
		f1.close()
		f2.close()
		f3.close()
		ver+=1
########################################################################
if z:
	for sub in comb:
		for zi in seq_z:
			#s1= "/home/lkit/wslap/data/A370/observation/tmp/tmp_theta_VER%d" %(ver)
			s1="/home/lkit/testing_tmp_theta"
			s2="/home/lkit/wslap/data/A370/observation/real_theta_VER%d" %(ver) 
			s3="/home/lkit/wslap/data/A370/observation/tmp/tmp_source_VER%d" %(ver)
			f1=open(s1,'w')
			f2=open(s2,'w')
			f3=open(s3,'w')
			count=1; level=1; flag=1
			tmp1=[]
			if stable: past=int((stable[0])[0]);
			if not stable: past=int((testing[0])[0]);
			#print 'past=',past
			if stable:
				for i in range(len(stable)):
					sys=int((stable[i])[0])			#system number
					if past!=sys: 			# turn system numbers to seq of natural number
						level+=1
						flag=1
					f1.write("%d\t\t%d\t\t%d\t\t%d\t\t%d\n" %(count,level,(stable[i])[1],(stable[i])[2],0))
					count+=1; past=sys
					f2.write("%.1f\n" %((stable[i])[0]))
					if flag==1:
						for ii in range(len(source)):
							#print int((source[ii])[0])
							if sys==int((source[ii])[0]): 
								tmp1.append(int((source[ii])[0]))
								break;

			flag=1
			if testing:
				for j in sub:
					sys=int((testing[j])[0])
					if past!=sys: 
						level+=1
						flag=1
					f1.write("%d\t\t%d\t\t%d\t\t%d\t\t%d\n" %(count,level,(testing[j])[1],(testing[j])[2],0))
					f2.write("%.1f\n" %((testing[j])[0]))
					count+=1; past=sys   
					if flag==1:
						for ii in range(len(source)):
							#print int((source[ii])[0])
							if sys==int((source[ii])[0]): 
								tmp1.append(int((source[ii])[0]))
			#tmp1=f7(tmp1)
			f3.write("\t\t%d\n" %len(tmp1)) 
			for k in range(len(tmp1)):
				f3.write("\t\t%d\t\t%d\t\t%d\t\t30\t\t%f\t\tsource_1.txt2\n" %(k+1,N_size/2,N_size/2,zi))   
			f1.close()
			f2.close()
			f3.close()
			ver+=1




print ver-1
        
        

