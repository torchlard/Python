import numpy as np
f=open("/home/lkit/Results/chema_selection.reg")
s=[]
for i in range(3):
    s.append(f.readline())

lists=[]
for line in f:
    m = re.search('circle\((.+)\)',line.strip())
    if m:
        lists.append(m.group(1).split(','))
f.close()

lists=np.asarray([[float(j) for j in i] for i in lists])
dx=4096-2823
dy=9803-4852
xcoor= lists[:,0]-dx
ycoor= lists[:,1]-dy

f=open("/home/lkit/tmp/do01.reg",'w')
for lines in s:
    f.write(lines)
for i in range(len(lists)):
    f.write('circle(%f,%f,%f)\n' %(xcoor[i],ycoor[i],lists[i,2]))
f.close()