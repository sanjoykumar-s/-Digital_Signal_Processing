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


duration = 1
t = makingT(duration,1000)
freq = 10 #hz
amp = 1
phase = 0
plt.subplot(2,2,1)
plt.plot(t,sineGen(freq,t,amp,phase),'r')
plt.title("Sine Wave at freq 10 Hz")
plt.xlabel('time')
plt.ylabel('Amplitute')

### Sampling using fs
fs = 40
ts = 1/fs
nt = nm.arange(0,duration,ts)

#sampling 1st wave having frequency 10 Hz
plt.subplot(2,2,2)
plt.stem(nt,samplingAtFs(freq,amp,phase,fs,duration),'b')
plt.title("Sampling-1")
plt.xlabel('time(n)')
plt.ylabel('Amplitute')
plt.grid()

freq = 50
plt.subplot(2,2,3)
plt.plot(t,sineGen(freq,t,amp,phase),'r')
plt.title("Sine Wave at freq 50 Hz")
plt.xlabel('time')
plt.ylabel('Amplitute')

#sampling 2nd wave having frequency 50 Hz
plt.subplot(2,2,4)
plt.stem(nt,samplingAtFs(freq,amp,phase,fs,duration),'b')
plt.title("Sampling-2")
plt.xlabel('time(n)')
plt.ylabel('Amplitute')
plt.grid()

plt.show()
