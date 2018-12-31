#!/usr/bin/env python

import numpy as np
import math

x = np.full(400, 0.0)
for i in range(20):
    tmp = math.sin((i+0.5)/20.0*math.pi)
    tmp *= tmp
    x[i+190] = math.sin(0.5*math.pi*tmp)

np.savetxt("window.dat", x)
