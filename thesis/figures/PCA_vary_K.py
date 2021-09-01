#%%
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')
from scipy.stats import gaussian_kde
import numpy as np

fname = 'ms_v1.npy'
# they should match!
Ks = np.arange(6, 32, step=4)

# np.save(fname, ms)
ms = np.load(fname)

x = np.linspace(min(np.log10(ms).flatten()), 0, num=400)

colors = plt.get_cmap('cividis')
for K, mismatch in zip(Ks[:-2], ms[:-2]):
    logm = np.log10(mismatch)
    kde = gaussian_kde(logm)
    plt.plot(x, kde(x), label=f'K={K}', color=colors(K/24))
    
    # plt.hist(logm, label=K, color=colors(K/ 27), alpha=.3)
plt.axvline(-3, ls=':', c='black')
plt.xlabel('Log-fidelity: $\\log_{10} \\mathcal{F}$')
plt.ylabel('Probability density, $\\dd{p} / \\dd{ \\log_{10} \\mathcal{F}}$')
plt.title('Reconstruction errors by number $K$ of principal components')
plt.legend()
plt.savefig('PCA_vary_K.pdf')

# %%
