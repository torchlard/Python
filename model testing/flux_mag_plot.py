import numpy as np
import matplotlib.pyplot as plt
import math

flux1=[3.454567,4.0425484,2.8186595,0.34168658,0.32283738,0.34052953]  #f475w[old]
noise1=[3.1537e-5,1.8263e-4,-2.2544e-4,-3.2489e-4,4.4379e-4,-3.1245e-5]
na1=[1388,1187,734,194,144,188]
ne1=[3649-1385,3067-1200,2809-1341,267,283,484]
rms1=0.00059001481
t1=18060.

flux2=[2.54858 ,3.0472208,1.9152368,0.25136217,0.21746042,0.28955571]  #f435w[new]
noise2=[1.5829e-4,1.783e-4,2.4181e-5,-9.521e-5,6.00803e-5,1.40664e-4] 
na2=[1385,1178,721,195,144,187]
ne2=[2844-1385,2308-1178,4065-721,636,515,544]
rms2=0.00059001481
t2=46260.

flux3=[48.435538,46.959979,31.339722,0.33510742,0.27747989,0.1512024]

#mag=[3.97882,6.6541,3.09998,4.07544,4.64381,2.49811]   #old model
#mag=[6.04132,7.63286,4.06299,5.72608,6.11397,4.22146]   #new model(4,9)
mag=[4.696,5.59632,3.51113,8.0118,23.1846,2.18474]   #VER75 (6,24)
#mag=[3.65096,8.81187,3.10495,4.0149,5.9389,2.30648]   #VER75 (4,9)



mag_ratio=[0]*6
flux_ratio=[0]*6
flux_mag=[0]*6
fw1=[0]*6
fw2=[0]*6
f_f1=[0]*3
f_f2=[0]*3
error1=[0]*6
error2=[0]*6
e1=[0]*3
e2=[0]*3

# def err1(i):
#     return math.sqrt((flux1[i]-noise1[i]*area1[i])/t1+(area1[i]+pow(area1[i],2)/ne1[i])*rms1/t1)
                     
# def err2(i):
#     return math.sqrt((flux2[i]-noise2[i]*area2[i])/t1+(area2[i]+pow(area2[i],2)/ne2[i])*rms2/t2)
for i in range(6):
    fw1[i]=flux1[i]-noise1[i]*na1[i]  #reduced noise flux
    fw2[i]=flux2[i]-noise2[i]*na2[i]


for i in range(6):
    mag_ratio[i]=mag[i]/mag[(i+1)%3+(i/3)*3]
    flux_ratio[i]=flux3[i]/flux3[(i+1)%3+(i/3)*3]
    flux_mag[i]=flux_ratio[i]/mag_ratio[i]
#     fw1[i]=flux1[i]; fw2[i]=flux2[i];

#     error1[i]=math.sqrt(fw1[i]/area1[i])  #error bar
#     error2[i]=math.sqrt(fw2[i]/area2[i])
#     error1[i]=err1(i)
#     error2[i]=err2(i)

# for i in range(3):
#     f_f1[i]=fw1[3+i]/fw1[2-i]  #flux ratio
#     f_f2[i]=fw2[3+i]/fw2[2-i]
#     e1[i]=math.sqrt(pow(error1[3+i],2)+pow(error1[2-i],2))
#     e2[i]=math.sqrt(pow(error2[3+i],2)+pow(error2[2-i],2))
#     print 3+i,2-i
# print 'error1= ',error1
# print 'error2= ',error2
# print 'e1= ',e1
# print 'e2= ',e2
# print 'fw1= ',fw1
# print 'fw2= ',fw2

x=range(6)
y=[1]*6
plt.figure()
plt.plot(x,mag_ratio,'o',label='magnification ratio')
plt.plot(x,flux_ratio,'o',label='flux ratio')
plt.plot(x,flux_mag,'o',label='flux ratio:mag ratio')
# plt.errorbar(x,f_f1,yerr=e1,fmt='o',label='f475w')
# plt.errorbar(x,f_f2,yerr=e2,fmt='o',label='f435w')
plt.axis([-1, 6,0,12])
plt.legend(loc='upper right', shadow=True)
plt.suptitle('new model',fontsize=20)
# plt.text(0.,0.2,'4.1/4.2')
# plt.text(1.,0.2,'4.2/4.3')
# plt.text(2.,0.2,'4.3/4.1')
# plt.text(3.,0.2,'9.1/9.2')
# plt.text(4.,0.2,'9.2/9.3')
# plt.text(5.,0.2,'9.3/9.1')
plt.text(0.,0.2,'6.1/6.2')
plt.text(1.,0.2,'6.2/6.3')
plt.text(2.,0.2,'6.3/6.1')
plt.text(3.,0.2,'24.1/24.2')
plt.text(4.,0.2,'24.2/24.3')
plt.text(5.,0.2,'24.3/24.1')
plt.plot(x,y)

plt.show()



