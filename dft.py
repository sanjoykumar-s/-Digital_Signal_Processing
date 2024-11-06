import numpy as nm
import matplotlib.pyplot as plt
import cmath as cm
import math

def dft(x,N):
    X = nm.zeros(N,dtype=complex)
    for m in range(N):
        for n in range(N):
            X[m] += x[n]*nm.exp(-2j*nm.pi*n*m/N)
    return X

def phaseCalc(X,N):
    phase = []
    for z in X:
        ph = cm.phase(nm.round(z.real)+nm.round(z.imag)*1j)
        phase.append(math.degrees(ph))
    return phase

def magCalc(X,N):
    M = []
    for z in X:
        mag = nm.sqrt(nm.square(z.real)+nm.square(z.imag))
        M.append(mag)
    return M

def idft(X,N):
    x = nm.zeros(N,dtype=complex)
    for n in range(N):
        for m in range(N):
            x[n] += X[m]*nm.exp(2j*nm.pi*n*m/N)
        x[n] /= N
    return x

x = [0.3535,0.3535,0.6464,1.0607,0.3535,-1.0607,-1.3535,-0.3535]
N = 8

X = dft(x,N)
print(X.round(3))
M = magCalc(X,N)
P = phaseCalc(X,N)
print(nm.round(M,3))
print(nm.round(P,3))
print(idft(X,N).round(4).real)
