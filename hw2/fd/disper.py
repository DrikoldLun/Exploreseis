# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:15:48 2018

@author: 35613
"""

import numpy as np
from numpy import arange, zeros
import matplotlib.pylab as plt

L = 1000
fdom = 34
c = 340
wavelen = c/fdom
dX = np.arange(0.05*wavelen,wavelen,0.1)
dt = np.min(dX)/c

def disper(dx,dt):
    k = 2*np.pi/wavelen
    return 2*np.arcsin(c*dt/dx*np.sin(k*dx/2))/(dt*k)

CC=[]
XPW=[]
for dx in dX:
    CC.append(disper(dx,dt))
    XPW.append(wavelen/dx)
    
fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(1,2,1)

ax1.plot(XPW,CC)
ax1.axhline(y=c, xmin=0, xmax=20, linewidth=1, color = 'black')
ax1.set_xlim(0,20)
ax1.set_ylim(0,400)
ax1.set_ylabel(r'Phase Velocity(m/s)', fontsize=10)
ax1.set_xlabel(r'Points in per wavelenth', fontsize=10)
ax1.set_title('dt='+'%.5f'%dt+'s')

dx = 0.1*wavelen
dtmax = dx/c
dT = np.arange(0,dtmax,1e-4)
CC1=[]
TT=[]
for dt in dT:
    CC1.append(disper(dx,dt))
    TT.append(dt)
    
ax2 =fig.add_subplot(1,2,2)
ax2.plot(TT,CC1)
ax2.axhline(y=c, xmin=0, xmax=10, linewidth=1, color = 'black')
ax2.set_ylabel(r'Phase Velocity(m/s)', fontsize=10)
ax2.set_xlabel(r'dt(s)', fontsize=10)
ax2.set_title('dx='+'%.1f'%dx+'m')
plt.show()
