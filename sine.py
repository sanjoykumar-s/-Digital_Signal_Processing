import numpy as nm
import matplotlib.pyplot as plt

def makingT(duration, N):
    return nm.linspace(0,duration,N)

def sineGen(freq,t,amp,phase):
    x = 2*nm.pi*freq*t
    sine = amp*nm.sin(x+phase)
    return sine

def samplingByFs(freq,amp,phase,fs,duration):
    ts = 1/fs
    nt = nm.arange(0,duration,ts)
    return sineGen(freq,nt,amp,phase)

def samplingByPoint(freq,amp,phase,N,duration):
    nt = nm.linspace(0,duration,N)
    return sineGen(freq,nt,amp,phase)


t = makingT(1,1000)
freq = 5 #hz
amp = 5
phase = 0
plt.plot(t,sineGen(freq,t,amp,phase),'r')
plt.title("Sine Wave")
plt.xlabel('time')
plt.ylabel('Amplitute')
plt.grid()
plt.show()
