#%%

from mlgw_bns.fd_waveform_generation import Parameters, EOB
from time import time
import matplotlib.pyplot as plt
from mlgw_bns.constants import MASS_SUM_SECONDS
from collections import defaultdict

import numpy as np

from tqdm import tqdm

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')


#%%
frequencies = np.geomspace(10, 100, num=15)

times_SPA = defaultdict(list)

lens_SPA = defaultdict(list)


p = Parameters(1, 500, 500, 0, 0)

add_dict = {
    'initial_frequency': f*MASS_SUM_SECONDS,   
}

eob_td = p.eob_td | add_dict
eob_fd = p.eob | add_dict

for f in tqdm(frequencies):
    
    for _ in range(10):
        t1 = time()
        f_spa, rhpf, ihpf, rhcf, ihcf = EOB.EOBRunPy(eob_fd)
        t2 = time()
        times_SPA[f].append(t2 - t1)
        lens_SPA[f].append(len(f_spa))

times_TD = defaultdict(list)
lens_TD = defaultdict(list)
for f in tqdm(frequencies):
    
    
    for _ in range(3):
        t1 = time()
        t, hpt, hct = EOB.EOBRunPy(eob_td)
        t2 = time()
        times_TD[f].append(t2-t1)
        lens_TD[f].append(len(t))


# %%
# plt.hist(times[5])

avgs_SPA = [np.average(times_SPA[f]) for f in frequencies]
stds_SPA = [np.std(times_SPA[f]) for f in frequencies]

avgs_TD = [np.average(times_TD[f]) for f in frequencies]
stds_TD = [np.std(times_TD[f]) for f in frequencies]

kwargs = {
    'capsize': 3,
    'marker': 'o',
    'ls': '',
}

plt.errorbar(frequencies, avgs_SPA,
            yerr=stds_SPA,
            c='black',
            label='SPA', **kwargs)

plt.errorbar(frequencies, avgs_TD,
            yerr=stds_TD,
            c='blue',
            label='TD', **kwargs)

plt.xscale('log')
plt.yscale('log')
plt.ylabel('Evaluation time [seconds]')
plt.xlabel('Initial frequency [Hz]')
plt.title('\\texttt{TEOBResumS} evaulation times')
plt.legend()
plt.grid('on')

plt.savefig('TEOBResumSPA_evaluation.pdf')

# %%

lengths_SPA = [np.average(lens_SPA[f]) for f in frequencies]
lengths_TD = [np.average(lens_TD[f]) for f in frequencies]

plt.loglog(frequencies, lengths_SPA, label='SPA')
plt.loglog(frequencies, lengths_TD, label='TD')
plt.legend()

# %%

from astropy.constants import codata2018 as ac
import astropy.units as u

nu = 1 / 4
M = 2.8 * u.Msun
M_c = nu ** (3 / 5) * M

f = frequencies * u.Hz

tau = (5 / 256 * (np.pi * f * (ac.G * M_c / ac.c ** 3)**(5/8))**(-8 / 3)).to(u.s)

plt.loglog(f, tau)
plt.grid('on')

plt.xlabel('Initial frequency [Hz]')
plt.ylabel('Duration [s]')

# So things make sense. 
# %%

eob_p = p.eob_td | {'initial_frequency': 1000 * MASS_SUM_SECONDS}    
t, hpt, hct = EOB.EOBRunPy(eob_p)

plt.plot(t[-200:] * MASS_SUM_SECONDS, hpt[-200:])
# %%
