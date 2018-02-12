import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#flux4_475=[3.454567,4.0425484,2.8186595]   #sys4(f475w,not-corrected)
#flux9_475=[0.34168658,0.32283738,0.34052953]  #sys9(f475w,not-corrected)
#flux4_435=[2.54858 ,3.0472208,1.9152368]   #sys4(f435w,not-corrected)
#flux9_435=[0.25136217,0.21746042,0.28955571]  #sys9(f435w,not-corrected)
#flux6_105=[48.435538,46.959979,31.339722]   #sys6(f105w,not-corrected)
flux1_435n=[3.547235,1.8575,4.1095]


t475=18060.
t435=46260.
flux6_814=[10.0,13.4,6.7]              #sys6(f814w,corrected)
flux4_475=[3.475,3.84,2.86]               #sys4(f475w,corrected)
flux9_475=[0.37736,0.2578,0.344123]                #sys9(f475w,corrected)
flux4_435=[2.339,2.58796,2.075]            #sys4(f435w,corrected)
flux9_435=[0.268211,0.212864,0.275426]     #sys9 (f435w,corrected)

area1_435=[1373,681,1441]
area4_435=[1251,1013,774]
area4_475=[1373,1076,777]
area9_435=[164,133,165]
area9_475=[160,97,149]
area6=[2435,5002,2630]

noise1_435=[0.01262/2905,0.7957/2402,0.2461/2883]
noise4_435=[ 0.000121582,0.000381260,3.94305e-05]
noise4_475=[-1.0e-5,1.6e-4,-1.6e-4]
noise9_475=[-0.0001963,0.000353,-5.317e-5]
noise9_435=[-5.3e-5,5.0e-5,6.0e-5]

mag1=[11.9527,12.1554,16.7595]
mag6=[5.97739,7.22626,4.99934]   #ver81(sys6)
mag4=[5.5329,6.53753,4.1253]   #ver81(sys4)
mag9=[5.85724,5.70405,3.2267]     #ver81(sys9)

err4_435=[0]*3
err4_475=[0]*3
err9_435=[0]*3
err9_475=[0]*3
error4_435=[0]*3
error4_475=[0]*3
error9_435=[0]*3
error9_475=[0]*3
mag_ratio1=[0]*3
mag_ratio4=[0]*3
mag_ratio6=[0]*3
mag_ratio9=[0]*3
flux_ratio1=[0]*3
flux_ratio6=[0]*3
flux_ratio9=[0]*3
flux_ratio4=[0]*3
flux_mag9=[0]*3
flux_mag6=[0]*3
flux_mag4=[0]*3
flux_mag1=[0]*3
flux1_435=[0]*3

for i in range(3):
    flux1_435[i]=flux1_435n[i]-noise1_435[i]*area1_435[i]

# for i in range(3):   #multiply exposure time
#     flux1_435[i]=flux1_435[i]*t435
#     flux4_435[i]=flux4_435[i]*t435
#     flux4_475[i]=flux4_475[i]*t475
#     flux9_435[i]=flux9_435[i]*t435
#     flux9_475[i]=flux9_475[i]*t475
#     noise4_435[i]=noise4_435[i]*t435
#     noise4_475[i]=noise4_475[i]*t475
#     noise9_435[i]=noise9_435[i]*t435
#     noise9_475[i]=noise9_475[i]*t475

for i in range(3): # gen. mag,flux ratio
    mag_ratio1[i]=mag1[i]/mag1[(i+1)%3]
    flux_ratio1[i]=flux1_435[i]/flux4_435[(i+1)%3]
    flux_mag1[i]=flux_ratio1[i]/mag_ratio1[i]
    mag_ratio4[i]=mag4[i]/mag4[(i+1)%3]
    flux_ratio4[i]=flux4_475[i]/flux4_475[(i+1)%3]
    flux_mag4[i]=flux_ratio4[i]/mag_ratio4[i]
    
for i in range(3):  # generate 1st step error
    err4_435[i]=sqrt(sqrt(pow(flux4_435[i],2)+pow(noise4_435[i]*area4_435[i],2)))
    err4_475[i]=sqrt(flux4_475[i]+noise4_475[i]*area4_475[i])
    err9_435[i]=sqrt(sqrt(pow(flux9_435[i],2)+pow(noise9_435[i]*area9_435[i],2)))
    err9_475[i]=sqrt(sqrt(pow(flux9_475[i],2)+pow(noise9_475[i]*area9_475[i],2)))
    
for i in range(3):  # generate error
    error4_435[i]=flux4_435[i]/flux4_435[(i+1)%3]*\
    sqrt(pow(err4_435[i]/flux4_435[i],2)+pow(err4_435[(i+1)%3]/flux4_435[(i+1)%3],2))
    error4_475[i]=(flux4_475[i]/flux4_475[(i+1)%3])*\
    sqrt(pow(err4_475[i]/flux4_475[i],2)+pow(err4_475[(i+1)%3]/flux4_475[(i+1)%3],2))
    error9_435[i]=flux9_435[i]/flux9_435[(i+1)%3]*\
    sqrt(pow(err9_435[i]/flux9_435[i],2)+pow(err9_435[(i+1)%3]/flux9_435[(i+1)%3],2))
    error9_475[i]=(flux9_475[i]/flux9_475[(i+1)%3])*\
    sqrt(pow(err9_475[i]/flux9_475[i],2)+pow(err9_475[(i+1)%3]/flux9_475[(i+1)%3],2))
#     mag_ratio6[i]=mag6[i]/mag6[(i+1)%3]
#     flux_ratio6[i]=flux6_814[i]/flux6_814[(i+1)%3]
#     flux_mag6[i]=flux_ratio6[i]/mag_ratio6[i]
    
#     mag_ratio9[i]=mag9[i]/mag9[(i+1)%3]
#     flux_ratio9[i]=flux9_475[i]/flux9_475[(i+1)%3]
#     flux_mag9[i]=flux_ratio9[i]/mag_ratio9[i]

for i in range(3):
#     mag_ratio1[i]=mag1[i]/mag2[2-i]   #4:9
#     mag_ratio2[i]=mag5[(i+2)%3]/mag2[2-i]   #6:9
#    mag_ratio3[i]=mag1[i]/mag5[(i+2)%3]   #4:6
#     flux_ratio1[i]=flux3[i]/flux4[2-i]   #4(435):9(435)
#     flux_ratio2[i]=flux5[(i+2)%3]/flux4[2-i]   #6:9
     flux_ratio[i]=flux4_435[i]/flux6_814[(i+2)%3]   #4:6
#     flux_ratio4[i]=flux1[i]/flux2[2-i]   #4(475):9(475)


    





x2=[0]*3; x3=[0]*3; x1=range(3)
for i in range(3):
    x2[i]=x1[i]+0.005
    x3[i]=x1[i]+0.01
y=[1]*3

print error4_475
#plt.figure()
plt.plot(x1,flux_ratio,'o',label='flux ratio')
# plt.plot(x1,mag_ratio4,'o',label='magnification ratio')
# plt.errorbar(x2,flux_ratio4,yerr=error4_475,fmt='o',label='flux ratio')
# plt.plot(x3,flux_mag4,'o',label='flux ratio:mag ratio')
# plt.plot(x1,mag_ratio1,'o',label='magnification ratio')
# plt.errorbar(x2,flux_ratio1,yerr=error4_475,fmt='o',label='flux ratio')
# plt.plot(x3,flux_mag1,'o',label='flux ratio:mag ratio')
plt.axis([-1, 3,0,0.5])    #control plot dimensions
plt.legend(loc='lower center', shadow=True, bbox_to_anchor=(0.5, -0.05),
          fancybox=True, ncol=3)
plt.suptitle('new model,filtered',fontsize=20)
# plt.text(0.,0.2,'4.1/4.2')
# plt.text(1.,0.2,'4.2/4.3')
# plt.text(2.,0.2,'4.3/4.1')
# plt.text(0.,0.2,'1.1/1.2')
# plt.text(1.,0.2,'1.2/1.3')
# plt.text(2.,0.2,'1.3/1.1')
# plt.text(0.,0.2,'9.1/9.2')
# plt.text(1.,0.2,'9.2/9.3')
# plt.text(2.,0.2,'9.3/9.1')
# plt.text(0.,0.2,'6.1/6.2')
# plt.text(1.,0.2,'6.2/6.3')
# plt.text(2.,0.2,'6.3/6.1')
# plt.text(3.,0.2,'24.1/24.2')
# plt.text(4.,0.2,'24.2/24.3')
# plt.text(5.,0.2,'24.3/24.1')

plt.text(0.,0.2,'l4.1/l6.3')
plt.text(1.,0.2,'m4.2/m6.1')
plt.text(2.,0.2,'r4.3/r6.2')
# plt.text(0.,0.2,'l6.3/l9.3')
# plt.text(1.,0.2,'m6.1/m9.2')
# plt.text(2.,0.2,'r6.2/r9.1')
# plt.text(0.,0.2,'l4.1/l9.3')
# plt.text(1.,0.2,'m4.2/m9.2')
# plt.text(2.,0.2,'r4.3/r9.1')
plt.text(-0.8,0.6,'1.2 1.3 1.1')
plt.text(-0.8,0.5,'4.1 4.2 4.3')
plt.text(-0.8,0.4,'6.3 6.1 6.2')
plt.text(-0.8,0.3,'9.3 9.2 9.1')

plt.plot(x1,y)
plt.show()
