import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin

def convolution(x,h):
    l1 = len(x)
    l2 = len(h)
    y = np.zeros(l1+l2-1)

    for n in range(l1+l2-1):
        for k in range(l1):
            if n-k>=0 and n-k<l2:
                y[n] += x[k]*h[n-k]
    return y

fs = 1000
cutoff_freq = 100

# Number of filter coefficients
num_taps = 15

#list of coefficients
fir_coef = firwin(num_taps,cutoff_freq,fs=fs,window='hamming')

t = np.arange(0,1.0,1/fs)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*200*t)

t = t[t<0.5]
x = x[:len(t)]

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.50t + 0.5sin(2π.200t))')

y = convolution(x,fir_coef)
t = np.linspace(0,0.5,len(y))

plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('y(n) = fir_filter(x(n))')

plt.show()