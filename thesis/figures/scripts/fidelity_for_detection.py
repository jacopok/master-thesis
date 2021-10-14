#%%

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')
          
F = np.logspace(-5, 0)

plt.loglog(F, 1 - (1 - F)** 3)
plt.grid('on')
plt.xlabel(r'Fidelity $\\mathcal{F}$')
plt.ylabel(r'Detection loss rate')

# %%
