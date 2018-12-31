#!/usr/bin/env python

import sys
import numpy as np

window = sys.argv[1]

x = np.loadtxt(window + ".dat")
#y = 20*np.log10(np.abs(np.fft.rfft(x)))
y = np.abs(np.fft.rfft(x))

np.savetxt("spectrum_" + window + ".dat", y)
