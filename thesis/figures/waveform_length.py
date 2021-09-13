#%%

from mlgw_bns.utils import *
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')

f0s = np.logspace(.5, 1.7, num=5000) * u.Hz

nyquist = 2 ** 11 * u.Hz
times = (1/ optimal_df_hz(f0s)).to(u.min)

plt.loglog(f0s, times, c='black')
ax = plt.gca()
ax2 = ax.twinx()

ax2.loglog(f0s, (times * nyquist).si, alpha=0.)

ax.set_xlabel(f'Initial frequency [{f0s.unit}]')
ax.set_ylabel(f'Waveform duration [{times.unit}]')
ax2.set_ylabel(f'Number of points at {2*nyquist:.0f} sampling')

ax.grid('on')

ax.set_title('Duration of waveforms')

plt.savefig('waveform_length.pdf', dpi=150)
# %%
