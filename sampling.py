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


duration = 0.01
t = makingT(duration,1000)
freq = 500 #hz
amp = 5
phase = 0
plt.subplot(2,1,1)
plt.plot(t,sineGen(freq,t,amp,phase),'r')
plt.title("Sine Wave")
plt.xlabel('time')
plt.ylabel('Amplitute')

### Sampling using fs
fs = 1500
ts = 1/fs
nt = nm.arange(0,duration,ts)

plt.subplot(2,1,2)
plt.stem(nt,samplingAtFs(freq,amp,phase,fs,duration),'b')
plt.title("Sampling")
plt.xlabel('time(n)')
plt.ylabel('Amplitute')
plt.grid()
plt.show()
