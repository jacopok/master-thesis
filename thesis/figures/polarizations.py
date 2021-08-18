#%%

import numpy as np
import matplotlib.pyplot as plt

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

# %%
