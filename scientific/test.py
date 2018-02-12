
f=open('/home/lkit/wslap/data/A370/fiducial/mass_map_A370.dat')
iii=[[map(float,line.split())] for line in f]
f.close()
for i in iii:
    print i
    if i[2]>0:
        print i[2]