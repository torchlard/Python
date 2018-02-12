# generate magnification values in fits format
# Inputs
from __future__ import division
from __future__ import print_function
import numpy as np
import math
import pyfits
import itertools
from multiprocessing import Pool
from astropy.cosmology import FlatLambdaCDM
from astropy import constants as const
import sys
from Progress import progress_bar as pbr

alpha_size = 1400   # linear size input deflection field
pix_scale = 5600*30/1000./1400.   # arcseconds per pixel
lens_z = 0.375   # lens redshift
fid_z = 5.0   # fiducial source redshift of input deflection field
src_z = 1.5865   # desired source redshift (1:0.806,4:1.275,9:1.5865,6:1.063,24:1.441)          <============================================


def Mag_func(daxdx, daxdy, daydx, daydy):
    mu = abs(1. / ((1. - daxdx) * (1. - daydy) - daxdy * daydx))
    return mu
    
def Mag_func_star(arguments):
    # Convert mag_func([daxdx, daxdy, daydx, daydy]) to mag_func(daxdx, daxdy, daydx, daydy) call
    return Mag_func(*arguments)

def Mag(z_src, alpha_x, alpha_y, z_lens=lens_z, z_fid=fid_z):
    # compute the lensing distance ratio
    d_ls1 = cosmo.angular_diameter_distance_z1z2(z_lens, z_src)
    d_s1 = cosmo.angular_diameter_distance(z_src)
    d_ls2 = cosmo.angular_diameter_distance_z1z2(z_lens, z_fid)
    d_s2 = cosmo.angular_diameter_distance(z_fid)
    D = (d_ls1 / d_s1) / (d_ls2 / d_s2)
    
    # compute the partial derivatives of alpha_x and alpha_y
    daxdy, daxdx = D * np.gradient(alpha_x)
    daydy, daydx = D * np.gradient(alpha_y)
    daxdx = np.reshape(daxdx, (1, np.size(daxdx)))
    daxdy = np.reshape(daxdy, (1, np.size(daxdy)))
    daydx = np.reshape(daydx, (1, np.size(daydx)))
    daydy = np.reshape(daydy, (1, np.size(daydy)))
    
    pool = Pool()
    mu = pool.map(Mag_func_star, itertools.izip(daxdx, daxdy, daydx, daydy))[0]
    mu = [i.value for i in mu]
    mu = np.reshape(mu, (alpha_size, alpha_size))
    pool.close()
    pool.join()
    
    return mu

min_ver=161     #<=======
max_ver=161     #<=======

VER=min_ver
total = max_ver-min_ver
# pbr.printProgress(0,total,prefix='Progress:',barLength=100)
     
for VER in range(min_ver,max_ver+1):

    
    alpha_x_path = '/home/lkit/wslap/data/A370/reconstruction/alpha_x_rad/recomp_alpha_x_rad_VER'+str(VER)+'.fits'   # type full path
    alpha_y_path = '/home/lkit/wslap/data/A370/reconstruction/alpha_y_rad/recomp_alpha_y_rad_VER'+str(VER)+'.fits'
    output_path_fig = '/home/lkit/tmp/critcurve_map_sys9_30mas_VER'+str(VER)+'.fits'   # type output path
    output_path_data='/home/lkit/magnification/VER'+str(VER)

    cosmo = FlatLambdaCDM(H0=70., Om0=0.3)

    im = pyfits.open(alpha_x_path)
    alpha_x = im[0].data / math.pi * 180. * 3600. / pix_scale
    im.close()

    im = pyfits.open(alpha_y_path)
    alpha_y = im[0].data / math.pi * 180. * 3600. / pix_scale
    im.close()

    mu = Mag(src_z, alpha_x, alpha_y)

    # coor1,4,6,9
    # coor=[[[484,781],[715,762],[758,755]],
    #  [[383,770],[652,774],[915,724]],
    #  [[386,748],[690,744],[842,714]],
    #  [[312,765],[688,773],[901,724]]]       # input target coordinates in 1400x1400 pix fov

    coor=[[[1938,3118],[2863,3051],[3033,3021]],
        [[1534,3082],[2606,3094],[3657,2893]],
        [[1540,2990],[2753,2984],[3367,2857]],
        [[1248,3060],[2753,2984],[3368,2857]]]

    f=open(output_path_data,'w')

    # print (VER,'\t|',end="\t")
    for j in coor:
        for i in j:
            im0=int(round((i[0]/5600)*alpha_size-alpha_size/2))
            im1=int(round((i[1]/5600)*alpha_size-alpha_size/2))
            f.write(str((mu[im1-1])[im0-1]))
            f.write('\t')
        f.write('\n')
    f.close()
    # pbr.printProgress(VER-min_ver,total,prefix='Progress:',barLength=100)

    hdu1 = pyfits.PrimaryHDU(mu)
    hdu1.writeto(output_path_fig,clobber=True)




