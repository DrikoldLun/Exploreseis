# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:30:28 2018

@author: 35613
"""
import numpy as np
from numpy import arange, zeros
import matplotlib.pylab as plt
import os
#medium parameters
L = 1000
fdom = 34
c = 340
wavelen = c/fdom
dx = 0.1*wavelen
dt = 0.5*dx/c

XX = arange(0,L+dx,dx)
TT = arange(0,1000*dt,dt)

xs = dx*int(len(XX)/2)
t0 = 0

#source
def srcf(x,t):
    if x != xs: return 0
    return -8*fdom*(t-t0)*np.exp(-(t-t0)**2/(16*fdom**2))

U = zeros([len(XX),len(TT)+1],dtype='double')

#simulation
for i in range(len(XX)):
    U[i,0] = 0
    U[i,1] = 0

for j in range(len(TT)):
    U[0,j] = 0
    U[len(XX)-1,j] = 0

for j in range(1,len(TT)):
    for i in range(1,len(XX)-1):
        U[i,j+1] = c**2*dt**2/dx**2*(U[i+1,j]-2*U[i,j]+U[i-1,j])+2*U[i,j]-U[i,j-1]+dt**2*srcf(dx*i,j*dt)

fig = plt.figure(figsize=(10,4))
ax1 =fig.add_subplot(1,2,1)
ax2 =fig.add_subplot(1,2,2)

ax1.plot(XX,U[:,0], 'r-', label='NT=0',linewidth=1.0)
ax1.plot(XX,U[:,200], 'b-', label='NT=200',linewidth=1.0)
ax1.plot(XX,U[:,400], 'c-', label='NT=400',linewidth=1.0)
ax1.plot(XX,U[:,600], 'k-', label='NT=600',linewidth=1.0)
ax1.set_ylabel(r'U', fontsize=20)
ax1.set_xlabel(r'X', fontsize=20)
ax1.set_xlim(0,1000)
ax1.legend(loc='upper right')

extent = [0,len(TT),0,len(XX)-1]
levels = arange(-0.5,0,0.01)
cs = ax2.contourf(U,levels,origin='lower',extent=extent,cmap=plt.cm.hot)
ax2.set_ylabel(r'NX', fontsize=20)
ax2.set_xlabel(r'NT', fontsize=20)
plt.show()
plt.close('all')
#gif
isgif = raw_input('make .gif file? y/n:')
if isgif != "y": exit(1)

imgorder=''
for nt in arange(0,len(TT)+1,10):
    nt = int(nt)
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(XX,U[:,nt], 'r-',linewidth=1.0)
    ax.set_ylabel(r'U', fontsize=20)
    ax.set_xlabel(r'X', fontsize=20)
    ax.set_xlim(0,1000)
    ax.set_ylim(-0.5,0)
    plt.savefig(str(nt)+'.png')
    imgorder = imgorder+str(nt)+'.png '
    plt.close('all')

os.system('convert -delay 10 '+imgorder+'result.gif')
os.system('rm *.png')
