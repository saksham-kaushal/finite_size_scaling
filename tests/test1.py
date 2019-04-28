import fssa
import numpy as np
import matplotlib.pyplot as plt

def mock_scaling_f(x):
	"""Mock scaling function"""
	return np.exp(-(x + 1.0)**2)

def mock_scaled_data(l, rho, rho_c=0.5, nu=2.5, zeta=1.5):
	"""Generate scaled data from mock scaling function"""
	return np.transpose(
		np.power(l, zeta / nu) *
		mock_scaling_f(
			np.outer(
				(rho - rho_c), np.power(l, 1 / nu)
			)
		)
	)
"""
#plot of scaling function
x = np.linspace(-4.0, 2.0, num=200)
fig, ax = plt.subplots()
ax.plot(x, mock_scaling_f(x), label=r'$\tilde{f}(x)$', rasterized=True)
ax.set_xbound(x.min(), x.max())
ax.set_ybound(0.0, 1.1)
ax.set_xlabel(r'$x$')
ax.legend()
plt.show()
"""

#plot of scaled data
ls = np.logspace(1, 3, num=5).astype(np.int)
rhos = np.linspace(-0.5, 0.8, num=20)

a = mock_scaled_data(ls,rhos)

fig, ax = plt.subplots()
for l_index, l in enumerate(ls):
    ax.plot(
        rhos, a[l_index, :],
        '-',
        label=r'${}$'.format(l),
        rasterized=True,
    )
ax.set_xbound(rhos.min(), rhos.max())
ax.set_xlabel(r'$\rho$')
ax.legend(title=r'$L$', loc='upper left')
plt.show()

da = a*0.1
ret = fssa.autoscale(ls, rhos, a, da, 0.5, 1.5, 2.5)
print(ret)

auto_scaled_data = fssa.scaledata(ls, rhos, a, da, ret.rho, ret.nu, ret.zeta)
fig, ax = plt.subplots()
ax.plot(
    auto_scaled_data.x.T, auto_scaled_data.y.T,
    '.',
)
ax.set_xbound(-4, 2)
ax.set_xlabel(r'$x$')
plt.show()
