import matplotlib.pyplot as plt
import fssa
import numpy as np
from cycler import cycler
import itertools
import seaborn as sns

#declare and assign values of rhos and sort them in increasing order to give final values in rhos.
rhos = np.array([0.0100, 0.0200, 0.0500, 0.0670, 0.0770, 0.0910, 0.1000, 0.1050, 0.1110, 0.1150, 0.1200, 0.1250, 0.1280, 0.1300, 0.1400, 0.1800, 0.2500, 0.5000, 1.0000])

#declare and assign system sizes
ls = np.array([4,6,8,10,12,18])

#create pallet of colours for different colours in the plot
palette = sns.cubehelix_palette(n_colors=ls.size, start=2.0, rot=0.35, gamma=1.0, hue=1.0, light=0.9, dark=0.1,)
#sns.palplot(palette)

#declare and assign values of y (a in this case) and dy (da in this case) and sort them according to corresponding rhos along each vector
a = np.array([[0.0000,0.0000,0.0002,0.0139,0.1044,0.7003,2.0103,3.6790,7.9973,12.4161,20.8839,31.8755,36.8680,39.5821,39.2465,11.6503,4.4018,1.2341,0.4995],[0.0000,0.0000,0.0005,0.0110,0.0553,0.3279,0.9559,1.8216,4.3373,8.7182,27.5199,74.7230,101.2190,106.7021,57.9285,11.4596,4.2612,1.1865,0.4748],[0.0000,0.0000,0.0004,0.0112,0.0550,0.3424,0.9864,2.0649,5.2752,9.8504,28.6214,118.1590,182.9655,182.1672,64.5618,11.7856,4.3530,1.1732,0.4670],[0.0000,0.0000,0.0002,0.0137,0.0602,0.3477,1.0912,2.3572,5.7241,10.6976,28.0421,128.6778,291.0500,276.1990,67.9234,11.3335,4.2755,1.1784,0.4657],[0.0000,0.0000,0.0005,0.0115,0.0583,0.3684,1.1879,2.3409,6.1108,11.0874,28.6055,121.7012,407.6491,376.7905,65.7465,11.0758,4.0679,1.2011,0.4840],[0.0000,0.0000,0.0004,0.0133,0.0620,0.3885,1.2569,2.6262,6.1768,11.4267,29.0007,116.4075,785.4435,655.9518,67.7884,11.3103,4.0961,1.1665,0.4706]])
da = np.array([[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001]])


#main work including auto scaling. Initial guess for rho, nu and zeta are the last three parameters of the function fssa.autoscale(). Print the function's output to to get final error analysis and values of parameters.
ret = fssa.autoscale(ls, rhos, a, da, 0.45, 0.35, -2.25)
print (ret)
auto_scaled_data = fssa.scaledata(ls, rhos, a, da, ret.rho, ret.nu, ret.zeta)

#work involving plotting using matplotlib
fig,ax=plt.subplots()
ax.set_prop_cycle(cycler('color', palette))
ax.plot(auto_scaled_data.x.T,auto_scaled_data.y.T,'.')
#plt.legend()
#ax.set_xbound(rhos.min(), rhos.max())
plt.show()

