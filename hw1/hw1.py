# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sat Sep 29 10:38:54 2018

@author: 35613
"""
#loc: Nanjing(32.04N 118.78E) 10.31km depth in crust
#model: crust1.0

import numpy as np
import cmath
import matplotlib.pylab as plt

#density
rho1 = 2.74
rho2 = 2.78
#Vs
Vs1 = 3.55
Vs2 = 3.65
#miu
miu1 = Vs1**2*rho1
miu2 = Vs2**2*rho2

N = 10000
dtheta = np.pi/2/(N-1)
theta = np.zeros(N) #incident angle
reco = np.zeros(N) #reflection coefficient
reE = np.zeros(N) #associated energy flux ratio
tranco = np.zeros(N) #transmission coefficient
tranE = np.zeros(N)

for i in range(N):
    theta[i] = i*dtheta
    p = np.sin(theta[i])/Vs1 #horizontal slowness
    yita1 = cmath.sqrt(1/Vs1**2-p**2) #vertical slowness
    yita2 = cmath.sqrt(1/Vs2**2-p**2)
    reco[i] = abs((miu1*yita1-miu2*yita2)/(miu1*yita1+miu2*yita2))
    reE[i] = reco[i]**2
    tranco[i] = abs(2*miu1*yita1/(miu1*yita1+miu2*yita2))
    tranE[i] = tranco[i]**2*rho2*Vs2/rho1/Vs1

theta = 180*theta/np.pi

plt.plot(theta,reco,'r',label='reflection coefficient')
plt.plot(theta,reE,'r--',label='reflection energy flux ratio')
plt.plot(theta,tranco,'b',label='transmission coefficient')
plt.plot(theta,tranE,'b--',label='transmission energy flux ratio')
plt.legend()
plt.show()
