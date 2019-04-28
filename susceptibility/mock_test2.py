import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import itertools
import fssa

ls = np.array([4,6,8,10,12,18])

rhos = np.array([0.0100, 0.0200, 0.0500, 0.0670, 0.0770, 0.0910, 0.1000, 0.1050, 0.1110, 0.1150, 0.1200, 0.1250, 0.1280, 0.1300, 0.1400, 0.1800, 0.2500, 0.5000, 1.0000])

a = np.array([[0.0000,0.0000,0.0002,0.0139,0.1044,0.7003,2.0103,3.6790,7.9973,12.4161,20.8839,31.8755,36.8680,39.5821,39.2465,11.6503,4.4018,1.2341,0.4995],[0.0000,0.0000,0.0005,0.0110,0.0553,0.3279,0.9559,1.8216,4.3373,8.7182,27.5199,74.7230,101.2190,106.7021,57.9285,11.4596,4.2612,1.1865,0.4748],[0.0000,0.0000,0.0004,0.0112,0.0550,0.3424,0.9864,2.0649,5.2752,9.8504,28.6214,118.1590,182.9655,182.1672,64.5618,11.7856,4.3530,1.1732,0.4670],[0.0000,0.0000,0.0002,0.0137,0.0602,0.3477,1.0912,2.3572,5.7241,10.6976,28.0421,128.6778,291.0500,276.1990,67.9234,11.3335,4.2755,1.1784,0.4657],[0.0000,0.0000,0.0005,0.0115,0.0583,0.3684,1.1879,2.3409,6.1108,11.0874,28.6055,121.7012,407.6491,376.7905,65.7465,11.0758,4.0679,1.2011,0.4840],[0.0000,0.0000,0.0004,0.0133,0.0620,0.3885,1.2569,2.6262,6.1768,11.4267,29.0007,116.4075,785.4435,655.9518,67.7884,11.3103,4.0961,1.1665,0.4706]])

da = np.array([[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001],[0.0015,0.0016,0.0017,0.0017,0.0017,0.0015,0.0014,0.0011,0.0010,0.0008,0.0006,0.0005,0.0004,0.0003,0.0003,0.0002,0.0002,0.0001,0.0001]])

#palette = sns.cubehelix_palette(n_colors=ls.size, start=2.0, rot=0.35, gamma=1.0, hue=1.0, light=0.9, dark=0.1,)

#print(np.tile(rhos,(len(a),1)))
#print(a)
for i in range(6):
	plt.plot(rhos,a[i],'-')
#rhosd = np.tile(rhos,(len(a),1))
#plt.plot(rhosd,a,'.')
plt.show() 
'''
rho_c = np.tile(0.25, (3, 3))
nu = np.tile(3.0, (3, 3))
zeta = np.tile(2.0, (3, 3))
rho_c[0, :] = [0.25, 0.5, 0.75]
nu[1, :] = [2.0, 2.5, 3.0]
zeta[2, :] = [1.0, 1.5, 2.0]

# re-scale data (manually)
scaled_data = list()
quality = list()
for i in range(3):
    my_scaled_data = list()
    my_quality = list()
    for j in range(3):
        my_scaled_data.append(
            fssa.scaledata(
                ls, rhos, a, da,
                rho_c[i, j], nu[i, j], zeta[i, j]
            )
        )
        my_quality.append(fssa.quality(*my_scaled_data[-1]))
    scaled_data.append(my_scaled_data)
    quality.append(my_quality)

# plot manually re-scaled data
fig, axes = plt.subplots(
    nrows=3, ncols=3, squeeze=True,
    #figsize=(8, 7),
    sharex=True, sharey=True,
)

for (i, j) in itertools.product(range(3), range(3)):
    ax = axes[i, j]
#    ax.set_prop_cycle(cycler('color', palette))
    my_scaled_data = scaled_data[i][j]
    for l_index, l in enumerate(ls):
        ax.plot(
            my_scaled_data.x[l_index, :], my_scaled_data.y[l_index, :],
            label=r'${}$'.format(l),
            rasterized=True,
        )
    ax.set_xbound(-5, 2)
    if i == 0:
        ax.set_title(
            r'$\rho_c = {}$'.format(rho_c[i, j]),
            position=(0.25, 0.65),
        )
    elif i == 1:
        ax.set_title(
            r'$\nu = {}$'.format(nu[i, j]),
            position=(0.25, 0.65),
        )
    elif i == 2:
        ax.set_title(
            r'$\zeta = {}$'.format(zeta[i, j]),
            position=(0.25, 0.65),
        )
    if i == 2:
        ax.set_xlabel(r'$x$')
        ax.set_xticks([-4, -2, 0, ])
    if j == 0:
        ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.text(
        0.1, 0.5,
        r'$S={:.1f}$'.format(quality[i][j]),
        transform=ax.transAxes,
    )

plt.show()

#0.25, 3, 1

'''


fig, ax = plt.subplots()

ret = fssa.autoscale(ls, rhos, a, da, 0.25, 3, -1.5)
auto_scaled_data = fssa.scaledata(ls, rhos, a, da, ret.rho, ret.nu, ret.zeta)

print (ret)

ax.plot(auto_scaled_data.x.T,auto_scaled_data.x.T,'.')
ax.set_xbound(-4, 10)

plt.show()


