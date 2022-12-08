# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:07:53 2022

@author: lmeyer
"""
#This code plots the total fluorescence for each anode type over time. This code
#relies significantly on calling in data files, so it will not work properly unless
#all these data files exist in this folder structure. These are easy to change, though. 


import pandas as pd
import matplotlib.pyplot as plt

#import fluorescene data files for each anode type
pitch = pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\2022-09-19 Si_pitch\Voltage hold\totals_pitch.csv') 

milled = pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\2022-07-20 Milled-Si_PC\Voltage hold\CSVs\total_milled.csv') 

pecvd_nmp = pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\PECVD_NMP_082422\Voltage hold\totals_NMP.csv') 

pitch_oct = pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\2022-10-17 PECVD-Si@pitch\Voltage hold\Oct_pitch_total.csv') 

pitch_march = pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\Si@pitch\Voltage hold\fluor_totals.csv') 

si_C=pd.read_csv(r'C:\Users\LMEYER\Documents\in situ Raman\si_carbon_dataset\2022-03-11 insitu_Raman_Si@C\Voltage hold\fluor_totals.csv') 



plt.figure(1)
plt.plot(pitch.iloc[:,0],pitch.iloc[:,1],'go',label='Pitch-coated PECVD-Sept.',markersize=8)
plt.plot(milled.iloc[:,0],milled.iloc[:,1],'co',label='Milled Si w/ PC',markersize=8)
plt.plot(pecvd_nmp.iloc[:,0],pecvd_nmp.iloc[:,1],'mo',label='NMP-functionalized PECVD',markersize=8)
plt.plot(pitch_oct.iloc[:,0],pitch_oct.iloc[:,1],'ko',label='Pitch-coated PECVD-Oct.',markersize=8)
plt.plot(pitch_march.iloc[:,0],pitch_march.iloc[:,1],'ro',label='Pitch-coated PECVD-Mar.',markersize=8)
plt.plot(si_C.iloc[:,0],si_C.iloc[:,1],'bo',label='Si_C',markersize=8)
plt.xlabel('Time (hr)',fontsize=14)
plt.ylabel('Intensity',fontsize=14)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
# plt.legend(fontsize=14,loc='upper center', bbox_to_anchor=(0.5, 1.60))
plt.ylim([0,4.5e8])
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\total_fluor_updated.png',dpi=1000)

plt.figure(2)
plt.plot(pitch.iloc[:,0],pitch.iloc[:,1],'go',label='Pitch-coated PECVD-Sept.',markersize=8)
plt.plot(milled.iloc[:,0],milled.iloc[:,1],'co',label='Milled Si w/ PC',markersize=8)
plt.plot(pecvd_nmp.iloc[:,0],pecvd_nmp.iloc[:,1],'mo',label='NMP-functionalized PECVD',markersize=8)
plt.plot(pitch_oct.iloc[:,0],pitch_oct.iloc[:,1],'ko',label='Pitch-coated PECVD-Oct.',markersize=8)
plt.plot(pitch_march.iloc[:,0],pitch_march.iloc[:,1],'ro',label='Pitch-coated PECVD-Mar.',markersize=8)
plt.plot(si_C.iloc[:,0],si_C.iloc[:,1],'bo',label='Si_C',markersize=8)
plt.xlabel('Time (hr)',fontsize=14)
plt.ylabel('Intensity',fontsize=14)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.ylim([0,0.5e8])
# plt.legend(fontsize=14,loc='upper center', bbox_to_anchor=(0.5, 1.60))
plt.savefig(r'C:\Users\LMEYER\Documents\in situ Raman\total_fluor_zoomed.png',dpi=1000)




