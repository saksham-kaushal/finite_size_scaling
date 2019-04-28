import matplotlib.pyplot as plt
import fssa
import numpy as np
from cycler import cycler
import itertools
import seaborn as sns

#declare and assign values of rhos and sort them in increasing order to give final values in rhos.
rhox = np.array([1.00000,0.50000,0.25000,0.18000,0.14000,0.13000,0.12800,0.12500,0.12000,0.11500,0.11100,0.10500,0.10000,0.09100,0.07700,0.06700,0.05000,0.02000,0.01000])
rhos = np.zeros((len(rhox)))
leng1=len(rhox)
for i in range(leng1):
	rhos[i]=rhox[leng1-1-i]
del rhox

#declare and assign system sizes
ls = np.array([4,6,8,10,12,18])

#create pallet of colours for different colours in the plot
palette = sns.cubehelix_palette(n_colors=ls.size, start=2.0, rot=0.35, gamma=1.0, hue=1.0, light=0.6, dark=0.2,)
#sns.palplot(palette)

#declare and assign values of y (a in this case) and dy (da in this case) and sort them according to corresponding rhos along each vector
ax = np.array([[0.11300,0.12862,0.17485,0.24806,0.51964,0.70632,0.74410,0.79431,0.87130,0.92141,0.94695,0.97144,0.98375,0.99365,0.99893,0.99981,1.00000,1.00000,1.00000],[0.06216,0.06999,0.09398,0.13155,0.28974,0.53734,0.61828,0.73815,0.87271,0.93661,0.95965,0.97866,0.98745,0.99520,0.99915,0.99984,0.99999,1.00000,1.00000],[0.03997,0.04560,0.06163,0.08602,0.18654,0.42989,0.53343,0.69335,0.85568,0.92605,0.95437,0.97709,0.98698,0.99504,0.99918,0.99985,1.00000,1.00000,1.00000],[0.02871,0.03253,0.04304,0.06099,0.13352,0.35028,0.48901,0.68959,0.84569,0.91808,0.94879,0.97431,0.98618,0.99490,0.99910,0.99981,1.00000,1.00000,1.00000],[0.02184,0.02486,0.03243,0.04594,0.09950,0.29496,0.45856,0.68426,0.84082,0.91379,0.94565,0.97312,0.98532,0.99463,0.99911,0.99982,0.99999,1.00000,1.00000],[0.01190,0.01355,0.01799,0.02528,0.05437,0.19084,0.42789,0.67987,0.83657,0.90977,0.94232,0.97049,0.98392,0.99442,0.99905,0.99981,0.99999,1.00000,1.00000]])
dax = np.array([[0.00010,0.00014,0.00018,0.00023,0.00028,0.00035,0.00043,0.00053,0.00065,0.00079,0.00096,0.00114,0.00135,0.00153,0.00166,0.00173,0.00173,0.00164,0.00149],[0.00010,0.00014,0.00018,0.00023,0.00028,0.00035,0.00043,0.00053,0.00065,0.00079,0.00096,0.00114,0.00135,0.00153,0.00166,0.00173,0.00173,0.00164,0.00149],[0.00010,0.00014,0.00018,0.00023,0.00028,0.00035,0.00043,0.00053,0.00065,0.00079,0.00096,0.00114,0.00135,0.00153,0.00166,0.00173,0.00173,0.00164,0.00149],[0.00010,0.00014,0.00018,0.00023,0.00028,0.00035,0.00043,0.00053,0.00065,0.00079,0.00096,0.00114,0.00135,0.00153,0.00166,0.00173,0.00173,0.00164,0.00149],[0.00010,0.00014,0.00018,0.00023,0.00028,0.00035,0.00043,0.00053,0.00065,0.00079,0.00096,0.00114,0.00135,0.00153,0.00166,0.00173,0.00173,0.00164,0.00149],[0.00010,0.00014,0.00018,0.00023,0.00028,0.00035,0.00043,0.00053,0.00065,0.00079,0.00096,0.00114,0.00135,0.00153,0.00166,0.00173,0.00173,0.00164,0.00149]])

a = np.zeros(ax.shape)
leng2=ax.shape[0]
leng3=ax.shape[1]
for i in range(leng2):
	for j in range(leng3):
		a[i][j]=ax[i][leng3-1-j]
del ax

da = np.zeros(dax.shape)
leng4=dax.shape[0]
leng5=dax.shape[1]
for i in range(leng4):
	for j in range(leng5):
		da[i][j]=dax[i][leng5-1-j]
del dax

#main work including auto scaling. Initial guess for rho, nu and zeta are the last three parameters of the function fssa.autoscale(). Print the function's output to to get final error analysis and values of parameters.
ret = fssa.autoscale(ls, rhos, a, da, 0.2, 0.4, -0.4)
print (ret)
auto_scaled_data = fssa.scaledata(ls, rhos, a, da, ret.rho, ret.nu, ret.zeta)

#work involving plotting using matplotlib
fig,ax=plt.subplots()
ax.set_prop_cycle(cycler('color', palette))
ax.plot(auto_scaled_data.x.T,auto_scaled_data.y.T)
#ax.set_xbound(rhos.min(), rhos.max())
plt.show()

