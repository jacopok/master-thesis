#%%

import numpy as np
import matplotlib.pyplot as plt
from functools import partial

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
sigma = 1600

tau = np.linspace(100, periods*T, num=N)

phi = -tau ** (5 / 8)

omega = 1 / T

phidot = np.gradient(phi, tau)

t0 = tau[np.searchsorted(phidot, -omega)]

A = tau ** (-1 / 4)

h = A * np.cos(phi)

sinus = .1 * np.cos(tau/T + np.pi)

select_taus = tau[::100]

# THIS ALSO WORKS: 
# exponential window

# def window(time, sigma):
#     return (np.exp(-(time)** 2 / sigma ** 2))

    
def window(time, sigma):
    return np.where(abs(time)<sigma, 1, 0)

w = partial(window, sigma=sigma)

integrals = [
    sum(sinus * h * w(tau-t))**2
    for t in select_taus
]

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].plot(tau, h, c='black', lw=.4, label='Waveform')
axs[0].plot(tau, sinus, c='black', ls=':', lw=.4, label='Fourier component')

axs[0].legend()

axs[1].plot(select_taus, integrals, c='black', label='Local integral contribution')


A = 60

axs[1].plot(tau, A * w(tau - t0), label='Window', c='black', ls=":")
axs[1].plot(tau, A * w(tau - t0 - 6000), c='black', ls=":")
axs[1].plot(tau,  A * w(tau - t0 + 6000), c='black', ls=":")
axs[1].axvline(t0, c='black', ls='--', label='$\\dot{\\Phi} = \\omega$')

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

plt.plot(-tau, phi)
# %%
