#%%

from mlgw_bns.utils import *
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib as mpl
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')

f0s = np.logspace(.6, 1.7, num=5000) * u.Hz

nyquist = 2 ** 11 * u.Hz
times = (1 / optimal_df(f0s)).to(u.min)
times_not_round = (1 / optimal_df(f0s, power_of_two=False)).to(u.min)

plt.loglog(f0s, times, c='black')
plt.loglog(f0s, times_not_round, c='black', ls='--')

ax = plt.gca()

ax2 = ax.twinx()

ax2.loglog(f0s, (times * nyquist).si, alpha=0.)

ax.set_xlabel(f'Initial frequency [{f0s.unit}]')
ax.set_ylabel(f'Waveform duration [{times.unit}]')
ax2.set_ylabel(f'Number of points at {2*nyquist:.0f} sampling')

ax.grid('on')

ax.set_title('Duration of waveforms')
ax.xaxis.set_major_formatter(mpl.ticker.EngFormatter())
ax.xaxis.set_minor_formatter(mpl.ticker.EngFormatter())

plt.savefig('waveform_length.pdf', dpi=150)
# %%
