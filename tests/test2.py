import fssa
import numpy as np
import matplotlib.pyplot as plt

ls = np.array([4,6,8,10,12,18])
data={}
for i in ls:
	fname = "../susceptibility/"+str(i)+"_w_0.0_X"
	data[i] = np.genfromtxt(fname)
rhosx = data[list(data.keys())[0]][:,0]
ax = np.array([data[i][:,1] for i in data.keys()])
dax = np.array([data[i][:,2] for i in data.keys()])

rhos=np.flip(rhosx)
a=np.flip(ax)
da=np.flip(dax)

#print(np.tile(rhos,(len(a),1)))

plt.plot(a,np.tile(rhos,(len(a),1)),'-')
plt.show()

ret = fssa.autoscale(ls, rhos, a, da, 0.15, 23.0, 5.0)
print(ret)

auto_scaled_data = fssa.scaledata(ls, rhos, a, da, ret.rho, ret.nu, ret.zeta)
fig, ax = plt.subplots()
ax.plot(
    auto_scaled_data.x.T, auto_scaled_data.y.T,
    '-',
)
#ax.set_xbound(-4, 2)
ax.set_xlabel(r'$x$')
plt.show()
