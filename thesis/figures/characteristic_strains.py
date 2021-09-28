import csv
from itertools import islice
from mlgw_bns import Model

import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('text.latex', preamble=r'''\usepackage{amsmath}
          \usepackage{physics}
          \usepackage{siunitx}
          ''')
import matplotlib as mpl
import numpy as np
# from mlgw_bns.plotting import plot_amp, plot_phase
import mlgw_bns.constants as const

from mlgw_bns.fd_waveform_generation import *

def main():

    m = Model('mid_freq', f0_hz=15)
    m.load()

    f_PSD = []
    H1_PSD = []
    L1_PSD = []
    V1_PSD = []

    with open('GWTC1_GW170817_PSDs.dat') as f:
        for line in islice(csv.reader(f, delimiter='\t'), 1, None):
            f_PSD.append(float(line[0]))
            H1_PSD.append(float(line[1]))
            L1_PSD.append(float(line[2]))
            V1_PSD.append(float(line[3]))
            
    f_PSD = np.array(f_PSD)
    L1_PSD = np.array(L1_PSD)
    H1_PSD = np.array(H1_PSD)
    V1_PSD = np.array(V1_PSD)

    f_psd_si = m.psd_f / const.MASS_SUM_SECONDS

    plt.loglog(f_psd_si, np.sqrt(f_psd_si * m.noise_psd('ET')), label='theoretical ET $h_n$', ls='--')
    plt.loglog(f_psd_si, np.sqrt(f_psd_si * m.noise_psd('aLIGO')), label='theoretical aLIGO $h_n$', ls='--')
    plt.loglog(f_PSD, np.sqrt(f_PSD * L1_PSD), label='actual Livingston $h_n$', lw=.5)
    plt.loglog(f_PSD, np.sqrt(f_PSD * H1_PSD), label='actual Hanford $h_n$', lw=.5)
    plt.loglog(f_PSD, np.sqrt(f_PSD * V1_PSD), label='actual Virgo $h_n$', lw=.5)

    f_amp_si = m.f_amp / const.MASS_SUM_SECONDS

    hp, _= m.predict_with_extrinsic(f_PSD, {
        'q': 1.16,
        'lambda1': 100,
        'lambda2': 400,
        's1z': 0.,
        's2z': 0.,
        'distance': 40 * 8.1,
    })

    plt.loglog(f_PSD, 2 * f_PSD * abs(hp), label='GW170817-like $h_c$', c='black')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Characteristic strain $h_c(f)$ or $h_n(f)$')

    # PSDs @ https://dcc.ligo.org/LIGO-P1900011/public

    plt.xlim(min(f_PSD), max(f_PSD))

    plt.legend()

    plt.savefig('characteristic_strains.pdf', dpi=150)
    plt.close()
    
    plt.plot(np.log(f_PSD), 4 * f_PSD * abs(hp)**2 /  L1_PSD, label='Livingston', lw=.5)
    plt.plot(np.log(f_PSD), 4 * f_PSD * abs(hp)**2 /  H1_PSD, label='Hanford', ls='--', lw=.5)
    plt.plot(np.log(f_PSD), 4 * f_PSD * abs(hp)**2 /  V1_PSD, label='Virgo', ls=':', lw=.5)

    plt.xlabel('Log-frequency [$\\log(f / 1 \\text{Hz})$]')
    plt.ylabel('$4 f \\abs{\\widetilde{h}}^2 / S_n = (h_c / h_n)^2$')
    plt.legend()
    plt.grid('on', lw=.4)
    plt.savefig('integrating_SNR.pdf', dpi=150)
    
if __name__ == "__main__":
    main()