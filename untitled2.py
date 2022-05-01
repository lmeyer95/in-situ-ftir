# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:03:35 2022

@author: lmeyer
"""

# importing pandas module 
import numpy as np
   




new_arr = np.array([[ 78,  23,  41,  66],
              [ 109,  167,  41,  28],
              [ 187, 22, 76, 88]])
b = new_arr.reshape(3, 2, 2)
print(b)

array1=np.zeros((36,894))
array2=array1.reshape(6,6,894)