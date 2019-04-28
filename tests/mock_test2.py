import matplotlib.pyplot as plt
import fssa
import numpy as np
from cycler import cycler
import itertools
import seaborn as sns

def mock_f(x):
	return np.exp(-(x+1)*(x+1))

def mock_data(l,rho,rho_c=0.5,nu=2.5,zeta=1.5):
	return np.transpose(np.power(l,zeta/nu)*mock_f(np.outer((rho-rho_c),np.power(l,1/nu))))

x = np.linspace(-4,2,num=100)

rhos = np.linspace(-0.5,0.8,num=100)
ls = np.logspace(1,3,num=5).astype(np.int)
# Define colors
palette = sns.cubehelix_palette(n_colors=ls.size, start=2.0, rot=0.35, gamma=1.0, hue=1.0, light=0.6, dark=0.2,)
#sns.palplot(palette)

a = mock_data(ls,rhos)
da = a*0.1
ret = fssa.autoscale(ls, rhos, a, da, 0.4, 1.8, 2.2)
print (ret)
auto_scaled_data = fssa.scaledata(ls, rhos, a, da, ret.rho, ret.nu, ret.zeta)


fig,ax=plt.subplots()
ax.set_prop_cycle(cycler('color', palette))
ax.plot(auto_scaled_data.x.T,auto_scaled_data.y.T,'.')
'''
for index,l in enumerate(ls):
	ax.plot(rhos,a[index,:])

ax.set_xbound(rhos.min(), rhos.max())
#ax.plot(x,mock_f(x))
'''
plt.show()

