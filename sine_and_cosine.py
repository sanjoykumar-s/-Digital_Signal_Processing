import numpy as nm
import matplotlib.pyplot as plt

amp = input("Amplitute = ")
freq = input("Frequency = ")
phase_in_deg = input("Phase (in degree) = ")

amp = float(amp)
freq = float(freq)
phase_in_deg = float(phase_in_deg)

phase_in_rad = phase_in_deg*nm.pi/180.0
t=nm.linspace(0,1,20000)
x = 2*nm.pi*freq*t
sine = amp*nm.sin(x+phase_in_rad)
cosine = amp*nm.cos(x+phase_in_rad)

plt.subplot(2,1,1)
plt.plot(t,sine,'r')
plt.title("Sine Wave")
plt.xlabel('time')
plt.ylabel('Amplitute')
plt.subplot(2,1,2)
plt.plot(t,cosine,'b')
plt.title("Cosine Wave")
plt.suptitle("Signal Generation")
plt.xlabel('time')
plt.ylabel('Amplitute')
plt.show()