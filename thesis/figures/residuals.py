from mlgw_bns import Model
from mlgw_bns.plotting import plot_amp, plot_phase
import numpy as np
import matplotlib.pyplot as plt

m = Model('spinning_6')
m.load()

N_plot = 30
N_ds = 128

ar, pd = m.reconstruction_errors(m.p[-N_plot:])

plot_phase(
    m.f[::N_ds],
    np.array(pd)[:,::N_ds],
    m.q[-N_plot:], 
    ylabel=r'Phase difference $\Phi_{\text{rec}} - \Phi_{\text{EOB}}$', 
    thr=8e-4, remove_linear=True)

plt.savefig('recon-phase-residuals.pdf')
plt.close()

plot_amp(m.f[::N_ds], np.array(ar)[:,::N_ds], m.q[-N_plot:], ylabel=r'Amplitude ratio $A_{\text{rec}} / A_{\text{EOB}}$')

plt.savefig('recon-amp-residuals.pdf')
plt.close()