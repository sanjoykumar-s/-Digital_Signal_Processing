import numpy as nm
import matplotlib.pyplot as plt

# Define transfer function coefficients
# Example: H(s) = (s^2 + 2s + 1) / (s^2 + s + 1)
# s = j*omega

neu_cof = [1,2,1]
deno_cof = [1,1,1]

freq = nm.logspace(-1, 2, 500)

M = []
P = []

for omega in freq:
    s = 1j*omega
    neu = sum(cof*(s**i) for i, cof in enumerate(reversed(neu_cof)))
    deno = sum(cof*(s**i) for i, cof in enumerate(reversed(deno_cof)))
    hs = neu/deno
    mg = nm.abs(hs)
    phs = nm.angle(hs)
    M.append(20*nm.log10(mg))
    P.append(nm.degrees(phs))

# Plot the magnitude response
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.semilogx(freq, M)  # Bode magnitude plot in dB
plt.title("Magnitude and Phase Response of H(s)")
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Magnitude [dB]")

# Plot the phase response
plt.subplot(2, 1, 2)
plt.semilogx(freq, P)  # Bode phase plot in degrees
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Phase [degrees]")

plt.tight_layout()
plt.show()