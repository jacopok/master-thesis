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

def evolve(t, x, y, h_p, h_c):
    expon = np.exp(1j * t * 2 * np.pi) / 2
    
    x_new = x * (1 + h_p * expon) + y * h_c * expon
    y_new = y * (1 - h_p * expon) + x * h_c * expon
    
    return (x_new, y_new)
    
thetas = np.linspace(0, 2 * np.pi)

xs = np.cos(thetas)
ys = np.sin(thetas)

ts = np.linspace(0, 1, num=20)

size = 3e-1
sizer = size / np.sqrt(2)
polarizations = {
    '$h_+$': [(0, 0), size, 0],
    '$h_\\times$': [(0, 1), 0, size],
    '$h_R$': [(1, 0), sizer, sizer * 1j],
    '$h_L$': [(1, 1), sizer, -sizer * 1j],
}

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, gridspec_kw={'wspace':-.5, 'hspace':0.25})

for k, v in polarizations.items():
    
    idx, h_p, h_c = v
    ax = axs[idx]
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    for t in ts:
        ax.plot(
            *evolve(t, xs, ys, h_p, h_c),
            c='black',
            alpha=t**4,
            lw=.5
        )
        ax.set_title(k)
    

plt.tight_layout()
fig.set_dpi(150)
fig.savefig('polarizations.pdf', bbox_inches = 'tight')
plt.close()

# %%

size_sm = 4e-1
polarizations_sm = {
    'h_p': [size_sm, 0, 0],
    'h_c': [0, size_sm, 1],
}

ts_sm = np.linspace(0, 4, num=50)
from tqdm import tqdm

for pol, v in polarizations_sm.items():

    h_p, h_c, to_add = v
    for i, t in tqdm(enumerate(ts_sm)):
        
        plt.plot(*evolve(t, xs, ys, h_p, h_c),
                c='black',
                lw=4,
                alpha=1
            )
        plt.plot(*evolve(1/2, xs, ys, h_p, h_c),
                alpha=0.
            )
        plt.plot(*evolve(0, xs, ys, h_p, h_c),
                alpha=0.
            )
        plt.gca().set_aspect('equal')
        plt.xticks([])
        plt.yticks([])
        plt.gca().set_axis_off()

        plt.tight_layout()
        plt.savefig(f'small_polarizations/{pol}-{2*i+to_add}.png')
        plt.close()
# %%
