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

N = 20000
T = 50
periods = 400

tau = np.linspace(100, periods*T, num=N)

phi = -tau ** (5 / 8)

A = tau ** (-1 / 4)

h = A * np.cos(phi)

sinus = .1 * np.cos(tau / T + np.pi)

select_taus = tau[::100]

integrals = [
    sum(sinus * h * np.exp(-(tau - t)**2 / 1500**2))**2
    for t in select_taus
]

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].plot(tau, h, c='black', lw=.4, label='Waveform')
axs[0].plot(tau, sinus, c='black', ls=':', lw=.4, label='Fourier transform contribution')

axs[0].legend()

axs[1].plot(select_taus, integrals, c='black', label='Local integral contribution')

axs[1].legend(loc='upper left')

axs[0].set_xlim(reversed(axs[0].get_xlim()))
axs[0].axes.xaxis.set_ticklabels([])
axs[0].axes.yaxis.set_ticklabels([])
axs[1].axes.yaxis.set_ticklabels([])

axs[1].set_xlabel('Decreasing $\\tau$')
# axs[0].set_ylabel('Waveform')
# axs[1].set_ylabel('Local integral contribution')

plt.tight_layout()
fig.savefig('spa.pdf', dpi=500)
# %%
