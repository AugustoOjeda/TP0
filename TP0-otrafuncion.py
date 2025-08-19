# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 18:36:22 2025

@author: Augusto
"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal
def mi_funcion_trian(vmax=1.0, dc=0.0, ff=1.0, ph=0.0, nn=1000, fs=1000.0, como_columna=True):
    tt = np.arange(nn, dtype=float) / float(fs)
    xx = dc + vmax * signal.sawtooth(2 * np.pi * ff * tt + ph)
    if como_columna:
        tt = tt.reshape(-1, 1)
        xx = xx.reshape(-1, 1)
    return tt, xx

if __name__ == "__main__":
    N = 1000
    fs = 1000

    casos = [(1, "1 Hz"),
             (4, "4 Hz"),
             (150, "150 Hz"),
             (500, "500 Hz"),
             (990, "990 Hz"),
             (1001, "1001 Hz"),
             (2001, "2001 Hz")]

    for ff, titulo in casos:
        tt, xx = mi_funcion_trian(vmax=1, dc=0, ff=ff, ph=0, nn=N, fs=fs, como_columna=False)
        plt.figure()
        plt.plot(tt, xx)
        plt.xlabel("tiempo [s]")
        plt.ylabel("Amplitud [V]")
        plt.title(f"Señal triangular: {titulo}")
        plt.show()