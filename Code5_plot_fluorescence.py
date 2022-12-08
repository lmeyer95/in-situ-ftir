# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:04:04 2022

@author: lmeyer
"""
#The purpose of this code is to plot fluorescence values over time for 
#one Raman mapping dataset. There are numerous variables in this code that 
#have to be changed for the code to be useful, but it could be a helpful
#starting place for making plots.



# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pybaselines


time=np.array([5,31,57,82,106,152,176]) #*User Input* Put in times of voltage hold
max_array=[] #initiate array of maximum fluorescence values
med_array=[] # initiate array of median fluorescence values
min_array=[] # initiate array of minimum fluorescence values

#################5hr#######################################
#input the folder from which you will import the Raman map dataset
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\5hr\CSVs'
#name the CSV for the coordinate with the maximum fluorescence value
max_file='spectra_VH_5H_[5. 5.].csv'
#name the CSV for the coordinate with the median fluorescence value
med_file='spectra_VH_5H_[-25.  25.].csv'
#name the CSV for the coordinate with the minimum fluorescence value
min_file='spectra_VH_5H_[-25.  15.].csv'

#designate import path for min, median and max coordinate spectra
max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  

#import spectra
max_f_spec_5hr=pd.read_csv(max_import_path, header = None)
med_f_spec_5hr=pd.read_csv(med_import_path, header = None)
min_f_spec_5hr=pd.read_csv(min_import_path, header = None)

#separate spectrum into x and y values
y=np.array(max_f_spec_5hr.iloc[:,1])
x=np.array(max_f_spec_5hr.iloc[:,0])
#use pybaselines to find background
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
#Use the trapezoid rule to measure the fluorescence background
area=np.trapz(bkg,x)
#input the fluorescence data into an array
max_array=np.append(max_array,area)
  
#repeat for median fluorescence coordinate
y=np.array(med_f_spec_5hr.iloc[:,1])
x=np.array(med_f_spec_5hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

#repeat for minimum fluorescence coordinate
y=np.array(min_f_spec_5hr.iloc[:,1])
x=np.array(min_f_spec_5hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)


#repeat these lines of code at all time steps in the voltage hold test
#################31hr#######################################
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\31hr\CSVs'
max_file='spectra_VH_31H_[5. 5.].csv'
med_file='spectra_VH_31H_[-25.  25.].csv'
min_file='spectra_VH_31H_[-25.  15.].csv'


max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  


max_f_spec_31hr=pd.read_csv(max_import_path, header = None)
med_f_spec_31hr=pd.read_csv(med_import_path, header = None)
min_f_spec_31hr=pd.read_csv(min_import_path, header = None)


y=np.array(max_f_spec_31hr.iloc[:,1])
x=np.array(max_f_spec_31hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
max_array=np.append(max_array,area)
  

y=np.array(med_f_spec_31hr.iloc[:,1])
x=np.array(med_f_spec_31hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

y=np.array(min_f_spec_31hr.iloc[:,1])
x=np.array(min_f_spec_31hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)
#################57hr#######################################
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\57hr\CSVs'
max_file='spectra_VH_57H_[5. 5.].csv'
med_file='spectra_VH_57H_[-25.  25.].csv'
min_file='spectra_VH_57H_[-25.  15.].csv'
# med_file2='spectra_VH_0H_[ 15. -15.].csv'


max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  
# med_import_path2= folder +'/'+ med_file2 


max_f_spec_57hr=pd.read_csv(max_import_path, header = None)
med_f_spec_57hr=pd.read_csv(med_import_path, header = None)
min_f_spec_57hr=pd.read_csv(min_import_path, header = None)
# med_f_spec_0hr2=pd.read_csv(med_import_path2, header = None)


y=np.array(max_f_spec_57hr.iloc[:,1])
x=np.array(max_f_spec_57hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
max_array=np.append(max_array,area)
  

y=np.array(med_f_spec_57hr.iloc[:,1])
x=np.array(med_f_spec_57hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

y=np.array(min_f_spec_57hr.iloc[:,1])
x=np.array(min_f_spec_57hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)

#################82hr#######################################
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\82hr\CSVs'
max_file='spectra_VH_82H_[5. 5.].csv'
med_file='spectra_VH_82H_[-25.  25.].csv'
min_file='spectra_VH_82H_[-25.  15.].csv'
# med_file2='spectra_VH_0H_[ 15. -15.].csv'


max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  
# med_import_path2= folder +'/'+ med_file2 


max_f_spec_82hr=pd.read_csv(max_import_path, header = None)
med_f_spec_82hr=pd.read_csv(med_import_path, header = None)
min_f_spec_82hr=pd.read_csv(min_import_path, header = None)
# med_f_spec_0hr2=pd.read_csv(med_import_path2, header = None)


y=np.array(max_f_spec_82hr.iloc[:,1])
x=np.array(max_f_spec_82hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
max_array=np.append(max_array,area)
  

y=np.array(med_f_spec_82hr.iloc[:,1])
x=np.array(med_f_spec_82hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

y=np.array(min_f_spec_82hr.iloc[:,1])
x=np.array(min_f_spec_82hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)
#################106hr#######################################
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\106hr\CSVs'
max_file='spectra_VH_106H_[5. 5.].csv'
med_file='spectra_VH_106H_[-25.  25.].csv'
min_file='spectra_VH_106H_[-25.  15.].csv'
# med_file2='spectra_VH_0H_[ 15. -15.].csv'


max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  
# med_import_path2= folder +'/'+ med_file2 


max_f_spec_106hr=pd.read_csv(max_import_path, header = None)
med_f_spec_106hr=pd.read_csv(med_import_path, header = None)
min_f_spec_106hr=pd.read_csv(min_import_path, header = None)
# med_f_spec_0hr2=pd.read_csv(med_import_path2, header = None)


y=np.array(max_f_spec_106hr.iloc[:,1])
x=np.array(max_f_spec_106hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
max_array=np.append(max_array,area)
  

y=np.array(med_f_spec_106hr.iloc[:,1])
x=np.array(med_f_spec_106hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

y=np.array(min_f_spec_106hr.iloc[:,1])
x=np.array(min_f_spec_106hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)
#################152hr#######################################
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\152hr\CSVs'
max_file='spectra_VH_152H_[5. 5.].csv'
med_file='spectra_VH_152H_[-25.  25.].csv'
min_file='spectra_VH_152H_[-25.  15.].csv'
# med_file2='spectra_VH_0H_[ 15. -15.].csv'


max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  
# med_import_path2= folder +'/'+ med_file2 


max_f_spec_152hr=pd.read_csv(max_import_path, header = None)
med_f_spec_152hr=pd.read_csv(med_import_path, header = None)
min_f_spec_152hr=pd.read_csv(min_import_path, header = None)
# med_f_spec_0hr2=pd.read_csv(med_import_path2, header = None)


y=np.array(max_f_spec_152hr.iloc[:,1])
x=np.array(max_f_spec_152hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
max_array=np.append(max_array,area)
  

y=np.array(med_f_spec_152hr.iloc[:,1])
x=np.array(med_f_spec_152hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

y=np.array(min_f_spec_152hr.iloc[:,1])
x=np.array(min_f_spec_152hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)
#################176hr#######################################
folder=r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\176hr\CSVs'
max_file='spectra_VH_176H_[5. 5.].csv'
med_file='spectra_VH_176H_[-25.  25.].csv'
min_file='spectra_VH_176H_[-25.  15.].csv'
# med_file2='spectra_VH_0H_[ 15. -15.].csv'


max_import_path = folder +'/'+ max_file  
med_import_path= folder +'/'+ med_file  
min_import_path= folder +'/'+ min_file  
# med_import_path2= folder +'/'+ med_file2 


max_f_spec_176hr=pd.read_csv(max_import_path, header = None)
med_f_spec_176hr=pd.read_csv(med_import_path, header = None)
min_f_spec_176hr=pd.read_csv(min_import_path, header = None)
# med_f_spec_0hr2=pd.read_csv(med_import_path2, header = None)


y=np.array(max_f_spec_176hr.iloc[:,1])
x=np.array(max_f_spec_176hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
max_array=np.append(max_array,area)
  

y=np.array(med_f_spec_176hr.iloc[:,1])
x=np.array(med_f_spec_176hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
med_array=np.append(med_array,area)

y=np.array(min_f_spec_176hr.iloc[:,1])
x=np.array(min_f_spec_176hr.iloc[:,0])
bkg= pybaselines.polynomial.modpoly(y,x, poly_order=3)[0]
area=np.trapz(bkg,x)
min_array=np.append(min_array,area)

###################plotting#######################################
#this figure plots the min, median, and maximum fluorescence values over time
plt.figure(1)
plt.plot(time,min_array,'ko',label='Low fluorescence',markersize=8)
plt.plot(time,med_array,'ro',label='Median fluorescence',markersize=8)
plt.plot(time,max_array,'bo',label='High fluorescence',markersize=8)
plt.xlabel('Time (hr)',fontsize=18)
plt.ylabel('Intensity',fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.legend(fontsize=14,loc='upper center', bbox_to_anchor=(0.5, 1.20))
# plt.ylim([0,2.5e7])
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\fluorescence_change.png',dpi=1000)
############Maxs#######
#this figure plots the spectra of the maximum fluorescence coordinate at 4
#different time stamps

# plt.figure(2)
# plt.plot(max_f_spec_0hr.iloc[:,0],max_f_spec_0hr.iloc[:,1],'r-',label='0hr')
# plt.plot(max_f_spec_49hr.iloc[:,0],max_f_spec_49hr.iloc[:,1],'y-',label='49hr')
# plt.plot(max_f_spec_119hr.iloc[:,0],max_f_spec_119hr.iloc[:,1],'g-',label='119hr')
# plt.plot(max_f_spec_171hr.iloc[:,0],max_f_spec_171hr.iloc[:,1],'b-',label='171hr')
# plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
# plt.ylabel('Intensity',fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14)
# plt.ylim([0,7000])
# plt.legend(fontsize=12,loc='upper right')
# plt.title('High fluorescence location',fontsize=20)
# plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\2022-07-20 Milled-Si_PC\Voltage hold\high_fluorescence.png',dpi=1000)

# ################Meds#####################################
#this figure plots the spectra of the median fluorescence coordinate at 4
#different time stamps
# plt.figure(3)
# plt.plot(med_f_spec_0hr.iloc[:,0],med_f_spec_0hr.iloc[:,1],'r-',label='0hr')
# plt.plot(med_f_spec_47hr.iloc[:,0],med_f_spec_47hr.iloc[:,1],'y-',label='47hr')
# plt.plot(med_f_spec_118hr.iloc[:,0],med_f_spec_118hr.iloc[:,1],'g-',label='118hr')
# plt.plot(med_f_spec_192hr.iloc[:,0],med_f_spec_192hr.iloc[:,1],'b-',label='192hr')
# plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
# plt.ylabel('Intensity',fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14)
# plt.ylim([0,7000])
# plt.legend(fontsize=12,loc='upper right')
# plt.title('Median fluorescence location',fontsize=20)
# plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\2022-09-19 Si_pitch\Voltage hold\med_fluorescence.png',dpi=1000)

# ################Mins#####################################
#this figure plots the spectra of the minimum fluorescence coordinate at 4
#different time stamps
# plt.figure(4)
# plt.plot(min_f_spec_0hr.iloc[:,0],min_f_spec_0hr.iloc[:,1],'r-',label='0hr')
# plt.plot(min_f_spec_47hr.iloc[:,0],min_f_spec_47hr.iloc[:,1],'y-',label='47hr')
# plt.plot(min_f_spec_118hr.iloc[:,0],min_f_spec_118hr.iloc[:,1],'g-',label='118hr')
# plt.plot(min_f_spec_192hr.iloc[:,0],min_f_spec_192hr.iloc[:,1],'b-',label='192hr')
# plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
# plt.ylabel('Intensity',fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14)
# plt.ylim([0,7000])
# plt.legend(fontsize=12,loc='upper right')
# plt.title('Low fluorescence location',fontsize=20)
# plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\2022-09-19 Si_pitch\Voltage hold\low_fluorescence.png',dpi=1000)

################5hr#####################################
#this figure plots the spectra of the the minimum, median, and maximum 
#fluorescence coordinates at the 5 hr timestamp
plt.figure(5)
plt.plot(min_f_spec_5hr.iloc[:,0],min_f_spec_5hr.iloc[:,1],'r-',label='Low')
plt.plot(med_f_spec_5hr.iloc[:,0],med_f_spec_5hr.iloc[:,1],'y-',label='Median')
plt.plot(max_f_spec_5hr.iloc[:,0],max_f_spec_5hr.iloc[:,1],'g-',label='High')
plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
plt.ylabel('Intensity',fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
# plt.ylim([0,1000])
plt.legend(fontsize=12,loc='upper right')
plt.title('Voltage hold: 0hr',fontsize=20)
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\five_hr_fluorescence.png',dpi=1000)

################57hr#####################################
#this figure plots the spectra of the the minimum, median, and maximum 
#fluorescence coordinates at the 57 hr timestamp
plt.figure(6)
plt.plot(min_f_spec_57hr.iloc[:,0],min_f_spec_57hr.iloc[:,1],'r-',label='Low')
plt.plot(med_f_spec_57hr.iloc[:,0],med_f_spec_57hr.iloc[:,1],'y-',label='Median')
plt.plot(max_f_spec_57hr.iloc[:,0],max_f_spec_57hr.iloc[:,1],'g-',label='High')
plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
plt.ylabel('Intensity',fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
# plt.ylim([0,1000])
plt.legend(fontsize=12,loc='upper right')
plt.title('Voltage hold: 49hr',fontsize=20)
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\57hr_fluorescence.png',dpi=1000)

################106hr#####################################
#this figure plots the spectra of the the minimum, median, and maximum 
#fluorescence coordinates at the 106 hr timestamp
plt.figure(7)
plt.plot(min_f_spec_106hr.iloc[:,0],min_f_spec_106hr.iloc[:,1],'r-',label='Low')
plt.plot(med_f_spec_106hr.iloc[:,0],med_f_spec_106hr.iloc[:,1],'y-',label='Median')
plt.plot(max_f_spec_106hr.iloc[:,0],max_f_spec_106hr.iloc[:,1],'g-',label='High')
plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
plt.ylabel('Intensity',fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
# plt.ylim([0,1000])
plt.legend(fontsize=12,loc='upper right')
plt.title('Voltage hold: 119hr',fontsize=20)
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\106hr_fluorescence.png',dpi=1000)

################176hr#####################################
#this figure plots the spectra of the the minimum, median, and maximum 
#fluorescence coordinates at the 176 hr timestamp
plt.figure(8)
plt.plot(min_f_spec_176hr.iloc[:,0],min_f_spec_176hr.iloc[:,1],'r-',label='Low')
plt.plot(med_f_spec_176hr.iloc[:,0],med_f_spec_176hr.iloc[:,1],'y-',label='Median')
plt.plot(max_f_spec_176hr.iloc[:,0],max_f_spec_176hr.iloc[:,1],'g-',label='High')
plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=18)
plt.ylabel('Intensity',fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
# plt.ylim([0,1000])
plt.legend(fontsize=12,loc='upper right')
plt.title('Voltage hold: 171hr',fontsize=20)
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\176hr_fluorescence.png',dpi=1000)

