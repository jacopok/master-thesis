#%%

import h5py
import matplotlib.pyplot as plt

h5 = h5py.File('data.h5')


# %%
plt.plot(h5['rpsi4_22']['Rpsi4_l2_m2_r00900.txt'][:, 6])
# %%
