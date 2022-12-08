# -*- coding: utf-8 -*-
#The purpose of this code is to take a raw data file from a Raman mapping 
#and convert it to 36 CSVs that are titled according to their coordinates in 
#the Raman map. This code has a few user inputs which are specified with 
# *USER INPUT* near the line which requires the input. This code will not work
#if the Raman has different resolution unless you change 'num_spec' and 'wn_length.'
# You have to build the file structure; it will not build it for you. 

"""
Created on Tue May  3 14:24:57 2022

@author: lmeyer
"""
#Pull in necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import matplotlib.pylab as plt
import os


hr=0 # *USER INPUT* hour of voltage hold
filename=r'C:\Users\LMEYER\Documents\in situ Raman\2022-12-5 Milled Si PC\Voltage hold\0hr\LM033_milled_Si_PC_0hr.csv' # *USER INPUT* name of file and location
num_spec=36 # *USER INPUT* number of spectra in file
wn_length=997 # *USER INPUT* number of wavenumbers in the file

###############################################################################

data = pd.read_csv(filename, header = None) #read the csv into the program

xy_coord=pd.DataFrame(data.iloc[1:num_spec+1,0:2]).reset_index(drop=True).to_numpy() #read in the xy coordinates
spectra=pd.DataFrame(data.iloc[1:num_spec+1,2:-1]).reset_index(drop=True).to_numpy() #read in the spectral data
wavenumber=pd.DataFrame(data.iloc[0,2:-1]).reset_index(drop=True).to_numpy() #make the wavenumber data into its own array


for i in range(len(xy_coord)):
    spec=np.transpose(np.vstack((wavenumber[:,0],spectra[i,:]))) #stack the wavenumber and spectral data together for each spectrum
    pd.DataFrame(spec).to_csv(r'C:\Users\LMEYER\Documents\in situ Raman\2022-12-5 Milled Si PC\Voltage hold\0hr\CSVs\spectra_VH_'+str(hr)+'H_'+ str(xy_coord[i,0:2])+'.csv', index=False,header=False)
    # *USER INPUT* change folder name but not filename