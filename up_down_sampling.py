import numpy as nm
import matplotlib.pyplot as plt

def makingT(duration, N):
    return nm.linspace(0,duration,N)

def sineGen(freq,t,amp,phase):
    x = 2*nm.pi*freq*t
    sine = amp*nm.sin(x+phase)
    return sine

def samplingAtFs(freq,amp,phase,fs,duration):
    ts = 1/fs
    nt = nm.arange(0,duration,ts)
    return sineGen(freq,nt,amp,phase)


duration = 0.1
t = makingT(duration,1000)
freq = 50 #hz
amp = 2
phase = 0
plt.subplot(2,2,1)
plt.plot(t,sineGen(freq,t,amp,phase),'r')
plt.title("Sine Wave")
plt.xlabel('time')
plt.ylabel('Amplitute')

### Sampling using fs
fs = 300
ts = 1/fs
nt = nm.arange(0,duration,ts)

plt.subplot(2,2,2)
plt.stem(nt,samplingAtFs(freq,amp,phase,fs,duration),'b')
plt.title("Sampling")
plt.xlabel('time(n)')
plt.ylabel('Amplitute')

#downsampling
m = 2
nt = nt[::m]
wv = samplingAtFs(freq,amp,phase,fs,duration)
wv = wv[::m]

plt.subplot(2,2,3)
plt.stem(nt,wv,'c')
plt.title("Down-Sampling by 2")
plt.xlabel('time(n)')
plt.ylabel('Amplitute')

#upsampling
l=2
nt = nm.linspace(0,duration,len(nt)*2)
nw = nm.zeros(len(nt))
nw[::l] = wv

plt.subplot(2,2,4)
plt.stem(nt,nw,'y')
plt.title("Up-Sampling by 2")
plt.xlabel('time(n)')
plt.ylabel('Amplitute')

plt.grid()
plt.show()
