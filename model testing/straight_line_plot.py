from __future__ import division
from matplotlib import pyplot as plt
from Progress import progress_bar as pbr

flux1=[1.59362551,3.9612432,3.701949]
flux4=[2.334964,2.6594655,2.1351422]
flux6=[9.843,14.494,12.506]
flux9=[0.2725,0.2041,0.264]



def ratios(arr):
    s=[]
    for i in range(len(arr)):
        s.append(arr[i-1]/arr[i])
    return s

def plots(mag,flux):
	arr_mag=[]; arr_flux=[]
	for i in mag:
		arr_mag.append(ratios(i))
	for i in flux:
		arr_flux.append(ratios(i))
	for i,j in zip(arr_flux,arr_mag):
		plt.plot(i,j,'o')
	y=range(4)
	x=y
	# print 'arr_mag= ',arr_mag
	# print 'arr_flux= ',arr_flux
	# print 'zip= ',zip(arr_flux,arr_mag)
	plt.plot(x,y)	#draw diagonal line
	plt.xlabel('flux ratio')
	plt.ylabel('magnification ratio')

min_ver=151
max_ver=157

for VER in range(min_ver,max_ver+1):        

	f = open('/home/lkit/magnification/VER'+str(VER))
	data=[map(float,line.split()) for line in f]
	f.close()
	mag1=data[0]
	mag4=data[1]
	mag6=data[2]
	mag9=data[3]
	# mag1=[5.1,17,14]
	# mag4=[4.3,5.2,3.9]
	# mag6=[3.7,6.5,6.4]
	# mag9=[4,5.8,5.4]
	plots([mag1,mag4,mag6,mag9],[flux1,flux4,flux6,flux9])
	# plt.savefig('/home/lkit/plots/scatter_plots/VER'+str(VER))
	plt.savefig('/home/lkit/plots/scatter_plots/VER'+str(VER))	
	plt.close()

	pbr.printProgress(VER-min_ver,max_ver-min_ver,prefix='Progress:',barLength=50)











