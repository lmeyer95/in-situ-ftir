# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:38:13 2022

@author: lmeyer
"""

#breaking the data up separately and then calling functions that I need; that seems the easiest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import matplotlib.pylab as plt


data = pd.read_csv('test_data.csv', header = None)

xy_coord=pd.DataFrame(data.iloc[1:37,0:2])
spectra=pd.DataFrame(data.iloc[1:37,2:-1]).reset_index(drop=True).to_numpy()
spectra_3D=spectra.reshape(6,6,894)
spectra_3D_flip=np.flipud(spectra_3D)
wavenumber=pd.DataFrame(data.iloc[0,2:-1]).reset_index(drop=True).to_numpy()

plt.plot(wavenumber,spectra_3D_flip[0,0,:])

data = pd.read_csv('test_data2.csv', header = None)
xy_coord=pd.DataFrame(data.iloc[1:37,0:2])
spectra=pd.DataFrame(data.iloc[1:37,2:-1]).reset_index(drop=True).to_numpy()
spectra_3D=spectra.reshape(6,6,894)
spectra_3D_flip2=np.flipud(spectra_3D)
wavenumber=pd.DataFrame(data.iloc[0,2:-1]).reset_index(drop=True).to_numpy()





data= pd.read_csv('test_data3.csv', header = None)
xy_coord=pd.DataFrame(data.iloc[1:37,0:2])
spectra=pd.DataFrame(data.iloc[1:37,2:-1]).reset_index(drop=True).to_numpy()
spectra_3D=spectra.reshape(6,6,894)
spectra_3D_flip3=np.flipud(spectra_3D)
wavenumber=pd.DataFrame(data.iloc[0,2:-1]).reset_index(drop=True).to_numpy()



pd.DataFrame(spectra_3D_flip2[0,0,:]).to_csv('sample2.csv')
pd.DataFrame(spectra_3D_flip[0,0,:]).to_csv('sample3.csv')






fig, axs = plt.subplots(6, 6)
axs[0, 0].plot(wavenumber,spectra_3D_flip[0,0,:],'tab:orange')
axs[0, 1].plot(wavenumber,spectra_3D_flip[0,1,:], 'tab:orange')
axs[0, 2].plot(wavenumber,spectra_3D_flip[0,2,:], 'tab:orange')
axs[0, 3].plot(wavenumber,spectra_3D_flip[0,3,:], 'tab:orange')
axs[0, 4].plot(wavenumber,spectra_3D_flip[0,4,:], 'tab:orange')
axs[0, 5].plot(wavenumber,spectra_3D_flip[0,5,:], 'tab:orange')
axs[1, 0].plot(wavenumber,spectra_3D_flip[1,0,:],'tab:orange')
axs[1, 1].plot(wavenumber,spectra_3D_flip[1,1,:], 'tab:orange')
axs[1, 2].plot(wavenumber,spectra_3D_flip[1,2,:], 'tab:orange')
axs[1, 3].plot(wavenumber,spectra_3D_flip[1,3,:], 'tab:orange')
axs[1, 4].plot(wavenumber,spectra_3D_flip[1,4,:], 'tab:orange')
axs[1, 5].plot(wavenumber,spectra_3D_flip[1,5,:], 'tab:orange')










#change columns and rows



