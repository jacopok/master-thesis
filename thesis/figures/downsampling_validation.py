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

n_train = 2 ** np.arange(0, 10)

val_amp_avg = np.array([
    10736.28,
    11003.57,
    7937.32,
    1693.89,
    1337.33,
    1061.31,
    883.91,
    30.01,
    35.41,
    16.28
])

val_amp_max = np.array([
    189197.92,
    272446.10,
    163968.74,
    122863.11,
    122863.11,
    123118.89,
    108067.47,
    1268.33,
    1709.42,
    1806.70,
])

val_phi_avg = np.array([
    118.06,
    93.04,
    83.03,
    57.80,
    20.17,
    17.38,
    5.05,
    3.39,
    1.67,
    1.23
])

val_phi_max = np.array([
    411.54,
    464.57,
    464.91,
    377.13,
    364.76,
    364.76,
    259.13,
    168.22,
    50.37,
    26.39,
])

n_points_amp = np.array([
    664,
    751,
    839,
    1147,
    1347,
    1626,
    1966,
    2337,
    2768,
    3293,
])

n_points_phi = np.array([
    605,
    614,
    662,
    747,
    823,
    880,
    968,
    1032,
    1100,
    1152
])

tol_amp = 1e-8
tol_phi = 1e-7

#%%

fig, axs = plt.subplots(2, 1, sharex=True, dpi=150)

# fig.figaspect(1)

axs[0].loglog(n_train, val_amp_avg * tol_amp, c='black', ls=':', label='Average')
axs[0].loglog(n_train, val_amp_max * tol_amp, c='black', label='Maximum')
axs[0].axhline(tol_amp, ls='--', c='black', label='Tolerance')

axs[0].set_ylabel(r'$\max \abs{\log (A / A _{\text{rec}})}$')

axs[1].loglog(n_train, val_phi_avg * tol_phi, c='black', ls=':', label='Average')
axs[1].loglog(n_train, val_phi_max * tol_phi, c='black', label='Maximum')
axs[1].axhline(tol_phi, ls='--', c='black', label='Tolerance')

axs[1].set_ylabel(r'$\max \abs{\phi - \phi _{\text{rec}}}$')

axs[1].set_xlabel('Training dataset size')

for ax in axs:
    ax.grid('on')
    ax.legend()
    # ax.set_aspect(aspect=.2)

fig.savefig('downsampling_validation.pdf')

#%%
plt.close()


plt.semilogx(n_train, n_points_amp, ls='--', c='black', label='Amplitude')
plt.semilogx(n_train, n_points_phi, ls=':', c='black', label='Phase')
plt.xlabel('Training dataset size')

plt.ylim(0, plt.ylim()[1])

plt.ylabel('Number of points')
plt.legend()
plt.grid()

plt.savefig('downsampling_npoints.pdf', dpi=150)

# %%
