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

limitexp = 8
e_log = np.linspace(-limitexp, limitexp)

es = np.exp(e_log) / (1 + np.exp(e_log))


def a(e):
    return(e ** (12 / 19) / (1 - e ** 2) * (1 + 121 / 304 * e ** 2)**(870 / 2299))

a_s = a(e)

plt.plot(es, a_s, c='black')
plt.yscale('log')
plt.xscale('logit')
plt.xlabel('Eccentricity $e$, logit scale')
plt.ylabel('A quantity proportional to the semimajor axis $a(e)$, log scale')
plt.grid('on')

e0 = .617

plt.scatter(e0, a(e0), c='black')
plt.text(e0, a(e0) / 3, 'Hulse-Taylor pulsar: $e=0.617$')

def ratio(e, pos):
    r = (1 / np.sqrt(1 - e ** 2))
    r = round(r) if (r > 3 or r < 1.1) else round(r, 1)
    return f'{r}:1'

ax2 = plt.gca().twiny()
ax2.plot(es, a_s, c='black', alpha=0)
ax2.set_xscale('logit')
ax2.xaxis.set_major_formatter(plt.FuncFormatter(ratio))

ax2.set_xlabel('Orbital aspect ratio')

plt.savefig('eccentricity.pdf', dpi=150)

# %%
plt.plot(e, np.sqrt(1-e**2), c='black')
plt.yscale('log')
plt.xscale('logit')
plt.xlabel('$e$, logit scale')
# plt.ylabel('$\\propto a(e)$, log scale')
plt.grid('on')

# %%
