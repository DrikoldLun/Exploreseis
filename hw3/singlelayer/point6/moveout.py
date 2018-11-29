#!/usr/bin/env python
import os,obspy
import numpy as np
import matplotlib.pylab as plt
n=3000
dist=8.
delta=0.01
seis=obspy.read('*.sac')
npts=int(seis[0].stats.sac.npts)
sta=np.zeros([len(seis),npts],dtype=np.double)
for i in range(len(seis)):
    sta[i]=obspy.read(str(i+1)+'.sac')[0].data.copy()
    sta[i]=sta[i]/sta[i].max()
#for i in range(len(sta)):
#    plt.plot(np.arange(npts),2.*i+sta[i])
#plt.show()
#plt.close('all')
t0=np.arange(18.5,23,0.1)
v0=np.arange(4,5,0.1)
value=np.zeros([len(t0),len(v0)])
seqt0=np.arange(0,npts*0.01,0.01)
stanew=np.zeros([len(seis),npts],dtype=np.double)
for x in range(len(t0)):
    t=t0[x]
    for y in range(len(v0)):
        v=v0[y]
        temp=np.zeros(1000,dtype=np.double)
        for i in range(len(sta)):
            tdelay=((i+1)*dist)**2/2./v**2/t
            tpp=t+tdelay
            seqt=seqt0*t/tpp
            stanew[i]=np.interp(seqt0,seqt,sta[i],left=0.,right=0.)
            stanew[i]=stanew[i]/np.fabs(stanew[i]).max()
            temp+=stanew[i][1500:2500]
        value[x,y]=temp.max()
max_index=value.argmax(axis=1)
xmax=np.argmax(value[range(len(value)),max_index])
ymax=max_index[xmax]
print(t0[xmax],v0[ymax])
t=t0[xmax]
v=v0[ymax]

for i in range(len(sta)):
    tdelay=((i+1)*dist)**2/2./v**2/t
    seqt=seqt0-tdelay
    stanew[i]=np.interp(seqt0,seqt,sta[i],left=0.,right=0.)
    stanew[i]=stanew[i]/np.fabs(stanew[i]).max()

fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
for i in range(len(stanew)):
    ax1.plot(2.*i+sta[i][:n]/np.fabs(sta[i]).max(),seqt0[:n])
    ax2.plot(2.*i+stanew[i][:n],seqt0[:n])
ax1.invert_yaxis()
ax2.invert_yaxis()
ax1.hlines(t,-1,9)
ax2.hlines(t,-1,9)
ax1.set_ylabel('time/s')
ax1.set_title('Before NMO')
ax2.set_title('After NMO')
plt.savefig('NMO1.pdf')
plt.show()
