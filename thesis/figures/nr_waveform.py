#%%

from gwpy.timeseries import TimeSeries

strain = TimeSeries.read('data.h5', format='hdf5.losc')
# %%
