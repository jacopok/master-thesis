#%%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')

np.random.seed(101)

N = 1000
x = np.linspace(0, 10, num=N)

yerr = np.random.normal(size=N, scale=3) + 5*np.cos(x/2) + np.exp(-x/4) * 40 

y = x * (x-5) * (x-8) + yerr

# plt.plot(x, y)

# %%

# from scipy.optimize import curve_fit

def poly(p):
    def f(x):
        return sum(x ** i * coeff for i, coeff in enumerate(p[::-1]))
    return f

n1, n2 = N // 4, 3 * N // 4

training = slice(n1, n2)

col = plt.get_cmap('inferno')

for deg in [2, 3, 5]:
    p, cov = np.polyfit(x[training], y[training], deg, cov='unscaled')
    
    t_err = np.sqrt(
        np.sum((poly(p)(x[n1:n2]) - y[n1:n2])** 2))
    
    v_err = np.sqrt(
        np.sum((poly(p)(x[:n1]) - y[:n1])** 2)
        +
        np.sum((poly(p)(x[n2:]) - y[n2:])** 2)
        )
    
    # label = f'deg: {deg}, train: {t_err:.0f}, val: {v_err:.0f}'
    label = f'degree {deg}'
    
    plt.plot(x, poly(p)(x), label=label, c=col((deg-1)/5))
    
plt.plot(x, y, alpha=.3, c='black')

plt.axvline(x[training][0], ls=':', ymax=.6, c='black')
plt.axvline(x[training][-1], ls=':', ymax=.6, c='black')

plt.ylim(min(y), max(y))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper center')
plt.savefig('underoverfit_polys.pdf')
plt.close()
# %%

degs = np.arange(1, 9)
t_errs = np.zeros_like(degs, dtype=np.float)
v_errs = np.zeros_like(degs, dtype=np.float)

for i, deg in enumerate(degs):
    p, cov = np.polyfit(x[training], y[training], deg, cov=True)

    t_errs[i] = np.sqrt(
        np.sum((poly(p)(x[training]) - y[training])** 2))
    v_errs[i] = np.sqrt(
        np.sum((poly(p)(x[:n1]) - y[:n1])** 2)
        +
        np.sum((poly(p)(x[n2:]) - y[n2:])** 2)
        )

plt.semilogy(degs, t_errs, label='Training error', c='black', ls='--')
plt.semilogy(degs, v_errs, label='Validation error', c='black')
plt.xlabel('Polynomial degree')
plt.ylabel('Sum of square differences')

plt.legend()
plt.savefig('underoverfit_errors.pdf')
plt.close()
# %%
