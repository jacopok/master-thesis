#%%

from mlgw_bns.plotting import plot_ms_hist
import matplotlib.pyplot as plt

import joblib

def filter(d, keys, aliases=None):
    return {
        k: v
        for k, v in d.items()
        if k in keys
    }

mismatches = joblib.load('mismatches_dictionary_allcases.pkl')
# these refer to 12Hz initial frequency, 
# specifically, the dataset `spinning_6`

keys = list(mismatches.keys())

aliases_by_psd = {
    'ET-MLGW\\_BNS': 'Einstein Telescope PSD',
    'aLIGO-MLGW\\_BNS': 'Advanced LIGO PSD',
    'ones-MLGW\\_BNS': 'Uniform PSD',
    'ET-TF2': 'Einstein Telescope PSD',
    'aLIGO-TF2': 'Advanced LIGO PSD',
    'ones-TF2': 'Uniform PSD',
 }
 
aliases_by_method = {
    'aLIGO-MLGW\\_BNS': 'MLGW\\_BNS',
    'aLIGO-TF2': 'TaylorF2 (5.5PN, 7.5PN tides)',
}
 
kwargs_by_psd = {
    'ET-MLGW\\_BNS': {'ls' : '--', 'c': 'black'},
    'aLIGO-MLGW\\_BNS': {'ls': '-.', 'c': 'black'},
    'ones-MLGW\\_BNS': {'ls': ':', 'c':'black'},
    'ET-TF2': {'ls' : '--', 'c': 'black'},
    'aLIGO-TF2': {'ls': '-.', 'c': 'black'},
    'ones-TF2': {'ls': ':', 'c':'black'},    
}

kwargs_by_method = {
    'aLIGO-MLGW\\_BNS': 'MLGW\\_BNS',
    'aLIGO-TF2': 'TaylorF2 (5.5PN, 7.5PN tides)',
}

# plot_ms_hist(
#     mismatches,
#     'Reconstruction errors',
#     kde=True,
#     aliases=aliases_by_psd)

# %%


plot_ms_hist(
    filter(
        mismatches,
        ['aLIGO-MLGW\_BNS', 'ones-MLGW\_BNS', 'ET-MLGW\_BNS'],
    ),
    title='MLGW\_BNS reconstruction errors with three PSDs',
    kde=True,
    aliases=aliases_by_psd,
    kwarg_dict=kwargs_by_psd)
    
plt.savefig('MLGW_BNS_reconstruction_varying_PSD.pdf', dpi=150)
plt.close()

# %%

plot_ms_hist(
    filter(
        mismatches,
        ['aLIGO-TF2', 'ones-TF2', 'ET-TF2'],
    ),
    title='TF2 reconstruction errors with three PSDs',
    kde=True,
    aliases=aliases_by_psd,
    kwarg_dict=kwargs_by_psd,
    )

plt.savefig('TF2_reconstruction_varying_PSD.pdf', dpi=150)
plt.close()

# %%

plot_ms_hist(
    filter(
        mismatches,
        ['aLIGO-TF2', 'aLIGO-MLGW\_BNS'],
    ),
    title='Reconstruction errors',
    kde=False,
    aliases=aliases_by_method,
)

plt.savefig('MLGW_BNS_vs_TF2.pdf', dpi=150)
plt.close()


# %%

# %%
