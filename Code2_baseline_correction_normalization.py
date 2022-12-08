# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:04:04 2022

@author: lmeyer
"""

#The purpose of this code is to apply a baseline correction to the Raman mapping
#data, which should remove the fluorescence background. This code can also normalize
#each spectrum to a specified peak. Note: each spectrum is normalized to the a 
#peak specified within it. All spectra are normalized to the same peak position, 
#though this peak could look different for each spectrum. Normalizing to one specific
#peak from a specific spectrum could be done with this code. User inputs are 
#specified with *USER INPUT*. This code creates a new folder with the same 
#folder name as the one from which you import spectra, except for it adds 
#'_pybaselines' afterwards. This code creates CSVs with identical names to those
#that you're importing to minimize confusion.

# -*- coding: utf-8 -"""

import pandas as pd
import numpy as np
from natsort import natsorted
import os
import matplotlib.pyplot as plt
import pybaselines
from pybaselines import utils


##############################################################################
################################ *USER INPUT* #################################
##############################################################################
# Input the folder from which spectra will be imported
args = {
    # Path to raw data
    'folder' : r'C:\Users\LMEYER\Documents\in situ Raman\2022-07-20 Milled-Si_PC\Voltage hold\CSVs\0hr\CSVs',
   
}

##############################################################################
##############################################################################
##############################################################################

def chCorrect(args):
    
    # make the folder that will contain the baselined data
    new_folder = args['folder']+'_pybaselines2'
    os.mkdir(new_folder)
    # load files and sort by counter using natsorted()
    files = os.listdir(args['folder'])
    files = natsorted(files)
    # iterate over the file names
    for file in files:
        # define your save and import file paths
        import_path = args['folder'] +'/'+ file
        # file_save_name = file.replace('.','_')
        file_save_name = file

        # # file_save_name = file_save_name.replace('_txt','.csv')
        save_path = new_folder + '/' + file_save_name
        #  load data and sort based on wavenumber
        test_data = pd.read_csv(import_path, header = None)
        
        points=np.array(test_data)
        #plot spectra with no baseline correction
        plt.figure(1)
        plt.plot(points[:,0],points[:,1])

        #separate the data file into x and y coordinates
        x=points[:,0] 
        y=points[:,1]
        #use Pybaselines to find and remove background
        #see Pybaselines docs to update this procedure
        bkg_1 = pybaselines.polynomial.modpoly(y, x, poly_order=3)[0] 
        #Correct the baseline by removing the background from the y values
        corrected_baseline=y-bkg_1

        baseline=corrected_baseline #baseline is all the baseline subtracted spectra put together
        #final_baseline=baseline # *USER INPUT* uncomment this line if you 
        #prefer no normalization
        final_baseline=baseline[:]/baseline[105] #*USER INPUT*normalize based on a specific peak, sapphire window (429 cm^-1)
        final_spec=np.transpose(np.vstack([x,final_baseline]))

        #plot baseline corrected spectra
        plt.figure(2)
        plt.plot(final_spec[:,0],final_spec[:,1])
        export = pd.DataFrame(final_spec) #export the data to a .csv file
        export.to_csv(save_path, index = None, header = None)
 # Call the function
chCorrect(args)

