# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:04:04 2022

@author: lmeyer
"""
#This code measures the fluorescence background for all coordinates in one 
#folder of CSVs. This code uses the Pybaselines algorithm used in Code2 to 
#calculate the fluorescence background. This code also exports an array of the 
#fluorescence values.


# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull
from natsort import natsorted
import os
import matplotlib.pyplot as plt
import pybaselines
from pybaselines import utils
from scipy.signal import savgol_filter as sgf



##############################################################################
################################ *USER INPUT* #################################
##############################################################################

#This is the folder of spectra for which you want to measure fluorescence
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\176hr\CSVs'
#This is the path where you want to save an array of fluorescence values
save_path=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\fluor_176hr.csv'
##############################################################################
##############################################################################
##############################################################################


    

    # make the folder that will contain the baselined data
    # new_folder = args['folder']+'_pybaseline_normalized'
    # os.mkdir(new_folder)
    # # load files and sort by counter using natsorted()
files = os.listdir(folder)
files = natsorted(files)
    # iterate over the file names
flor_bkg=np.array(files)
bkg_val=[]
for file in files:
  import_path = folder +'/'+ file  
  test_data = pd.read_csv(import_path, header = None)   
  points=np.array(test_data)  
  wn=pd.DataFrame(test_data.iloc[:,0])


  x=points[:,0]
  y=points[:,1]
  bkg_1 = pybaselines.polynomial.modpoly(y, x, poly_order=3)[0]
  area=np.trapz(bkg_1,x)
  bkg_val=np.append(bkg_val,area)
  plt.figure(2)
  plt.plot(x,y)

fluor_vals=np.transpose(np.vstack([flor_bkg,bkg_val]))  
export=pd.DataFrame(fluor_vals)
export.to_csv(save_path, index = None, header = None)


max_f=max(bkg_val)
max_loc=np.where(bkg_val==max_f)
max_f_coord=fluor_vals[max_loc,0]


min_f=min(bkg_val)
min_loc=np.where(bkg_val==min_f)
min_f_coord=fluor_vals[min_loc,0]

med_array=np.delete(bkg_val,max_loc)
med_f=np.median(med_array)
med_loc=np.where(bkg_val==med_f)
med_f_coord=fluor_vals[med_loc,0]


























# ##############################################################################
# ################################ USER INPUTS #################################
# ##############################################################################
# =pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\test_data\baseline analysis\mesh_electrode_data_-25_-25_5h.csv',header=None)



# ##############################################################################
# ##############################################################################
# #############################################################################ll

