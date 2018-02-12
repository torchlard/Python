import sys

f=open('/home/lkit/wslap/data/current_version')
for line in f: total=int(line);
f.close()

#print 'total= ',total
#total=31
ori=[]
for i in range(total):
    s='/home/lkit/wslap/data/A370/observation/real_theta_VER%d' %(i+1)
    f=open(s)
    ori.append([])
    for line in f: 
        ori[i].append(float(line))
    f.close()


match=[1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 5.3,
       6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 7.4, 7.5, 8.1, 8.2, 8.3, 9.1, 9.2, 9.3]	#stable images
extra=raw_input("extra images except sys (1-9) :")

vec=[float(x) for x in extra.split()]
for i in vec: match.append(i);
#print match

for i in range(total):
    #print ori[i-1]
    if len(ori[i-1])==len(match):
        #print "yes"
        #print set(ori[i-1])&set(match)
        if (len(set(ori[i-1])&set(match))==len(match)):
            print "ver= ",i
            break;









