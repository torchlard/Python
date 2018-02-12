from photutils.background import Background
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from astropy.stats import biweight_location
from astropy.stats import sigma_clipped_stats
from astropy.io import fits
import matplotlib.pylab as plt
import numpy as np

x1=2561; x2=2651
y1=3037; y2=3159

dat=np.zeros((x2-x1,y2-y1))

f=fits.open('/home/lkit/Data/Jan_data/30mas_v0.5_f435w.fits')
for i in xrange(x1,x2):
    for j in xrange(y1,y2):
        dat[i-2561,j-3037]=(f[0].data[i])[j]
f.close()


bkg = Background(dat, (80, 50), filter_shape=(3, 3), method='median')
print(bkg.background_median)
plt.imshow(bkg.background, origin='lower', cmap='Greys_r')
plt.show()

# data = make_100gaussians_image()
# norm = ImageNormalize(stretch=SqrtStretch())
# plt.imshow(data, origin='lower', cmap='Greys_r', norm=norm)
# plt.show()
# print(np.median(data))
# print biweight_location(data)

# mean, median, std = sigma_clipped_stats(data, sigma=3.0, iters=5)
# print((mean, median, std))
