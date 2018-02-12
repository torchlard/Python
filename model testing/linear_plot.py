from __future__ import division
from matplotlib import pyplot as plt
from Progress import progress_bar as pbr

#-------driver model--------
# mag1=[5.1,17,14]
# mag4=[4.3,5.2,3.9]
# mag6=[3.7,6.5,6.4]
# mag9=[4,5.8,5.4]
#-------my model--------------
# mag1=[44.5968,12.0977,124.922]
# mag4=[14.98,26.0772,9.9501]
# mag6=[19.1,10.5358,32.8214]
# mag9 = [13.68,9.89,11.77]
#-------Gold+silver system-----
# mag1=[6.3,19,14]
# mag4=[5.3,5.4,4.9]
# mag6=[4.3,7.9,7.3]
# mag9=[4.8,6.2,7]

flux1=[1.59362551,3.9612432,3.701949]
flux4=[2.334964,2.6594655,2.1351422]
flux6=[9.843,14.494,12.506]
#flux9=[1.5594254,3.87117544,3.758614]
flux9=[0.2725,0.2041,0.264]
#================================
def ratios(arr):
    s=[]
    for i in range(len(arr)):
        s.append(arr[i-1]/arr[i])
    return s
x=range(3)
axis=["1.3/1.1","1.1/1.2","1.2/1.3"]

def plots(arr,color):
    n=len(arr)
    i=0
    for sub in arr:
        x=range(0+3*i,3+3*i)
        plt.plot(x,ratios(sub),'o',c=color)
        i+=1
    plt.axis([-0.5,-0.5+3*n,-0.5,3])

def axis(arr):
    count=0
    for j in arr:
        x=str(j)
        xaxis=[x+".3/"+x+".1",x+".1/"+x+".2",x+".2/"+x+".3"]
        for i in xaxis:
            plt.text(count-0.25,0.2,i,fontsize=10)
            count+=1

min_ver=161       #<=========
max_ver=161      #<=========

for VER in range(min_ver,max_ver+1):        

    f = open('/home/lkit/magnification/VER'+str(VER))
    data=[map(float,line.split()) for line in f]
    f.close()
    mag1=data[0]
    mag4=data[1]
    mag6=data[2]
    mag9=data[3]
    plots([mag1,mag4,mag6,mag9],'y')
    plots([flux1,flux4,flux6,flux9],'b')
    x=range(0,12)
    y=[1]*12
    plt.plot(x,y)
    axis([1,4,6,9])
    plt.savefig('/home/lkit/plots/linear_plots/VER'+str(VER))
    plt.close()

    # pbr.printProgress(VER-min_ver,max_ver-min_ver,prefix='Progress:',barLength=50)    

# plt.suptitle('Driver model(blue=flux ratio,yellow=magnification ratio)',fontsize=20)
# print ratios(flux9)