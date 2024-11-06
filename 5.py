import numpy as np
import matplotlib.pyplot as plt

# Define transfer function coefficients
# Example: H(s) = (s^2 + 2s + 1) / (s^2 + s + 1)
numerator_coeffs = [1, 2, 1]   # Coefficients for s^2 + 2s + 1
denominator_coeffs = [1, 1, 1]  # Coefficients for s^2 + s + 1

# Define a range of angular frequencies (in rad/s)
frequencies = np.logspace(-1, 2, 500)  # Range from 0.1 to 100 rad/s
print(frequencies)

# Initialize lists to store magnitude and phase responses
magnitudes = []
phases = []

# Loop over each frequency
for omega in frequencies:
    # Calculate s = j * omega
    s = 1j * omega
    
    # Calculate the numerator and denominator of H(s) at this frequency
    numerator = sum(coef * s**i for i, coef in enumerate(reversed(numerator_coeffs)))
    denominator = sum(coef * s**i for i, coef in enumerate(reversed(denominator_coeffs)))
    
    # Calculate H(s) = numerator / denominator
    H_s = numerator / denominator
    
    # Compute magnitude and phase of H(s)
    magnitude = abs(H_s)
    phase = np.angle(H_s)  # Phase in radians
    
    # Store results
    magnitudes.append(20 * np.log10(magnitude))  # Convert to dB
    phases.append(np.degrees(phase))  # Convert to degrees

# Plot the magnitude response
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitudes)  # Bode magnitude plot in dB
plt.title("Magnitude and Phase Response of H(s)")
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Magnitude [dB]")

# Plot the phase response
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phases)  # Bode phase plot in degrees
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Phase [degrees]")

plt.tight_layout()
plt.show()
