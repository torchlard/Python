import re
import sys

total_file=len(sys.argv)
for kk in range(1,total_file):
	filestr=str(sys.argv[kk])

	f=open(filestr)
	l= [line for line in f] 
	f.close()
	skip=[]
	count=0
	for line in l:
	    if line=='\n':
	        skip.append(count)
	    count+=1

	for i in range(len(skip)-1):
	    first,last=skip[i],skip[i+1]
	    if (last-first)>2:
	        for j in range(first,last-1):
	            l[j]=re.sub('\n','',l[j])
	        l[last+1]=re.sub('\n','',l[last+1])

	filestr=re.sub('.txt','',filestr)
	            
	f=open(filestr+'__.txt','w')
	for i in l:
	    f.write(i)
	f.close()   

