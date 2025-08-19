# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 18:36:22 2025

@author: Augusto
"""

import numpy as np
import matplotlib.pyplot as plt 
N=1000 
f=1
fs=1000
t=np.arange(N)/fs
Y=np.sin(2*np.pi*f*t)
# E=(1/N)*np.sum(Y**2)
# V=np.var(Y)
plt.xlabel('tiempo [segundos]')
plt.ylabel('Amplitud [V]')
z=plt.plot(t,Y)
