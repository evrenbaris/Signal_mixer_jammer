import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Parameters
fs = 1e4  # Sampling frequency (10 kHz)
t = np.arange(0, 1, 1/fs)  # Time axis (1 second)
target_freq = 50  # Target signal frequency (50 Hz)
jammer_freq = 80  # Jammer signal frequency (80 Hz)

# Target Signal (Sine wave)
target_signal = np.sin(2 * np.pi * target_freq * t)

# Jammer Signal (Sine wave with phase shift)
jammer_signal = 1.2 * np.sin(2 * np.pi * jammer_freq * t + np.pi/4)

# Adding Noise
noise_power = 0.2  # Noise power
noise = np.sqrt(noise_power) * np.random.normal(size=len(t))

# Mixed Signal\; combination of target, jammer, and noise
mixed_signal = target_signal + jammer_signal + noise

# Function for Frequency Analysis (FFT)
def plot_fft(signal, fs, title):
    n = len(signal)
    f = np.linspace(0, fs/2, n//2)  # Frequency axis
    fft_values = fft(signal)
    magnitude = 2/n * np.abs(fft_values[:n//2])  # Magnitude spectrum

    plt.figure(figsize=(12, 6))
    plt.plot(f, magnitude, label=title)
    plt.title(f"{title} - Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.legend()
    plt.show()

# Visualization
plt.figure(figsize=(12, 10))

# Target Signal
plt.subplot(4, 1, 1)
plt.plot(t[:500], target_signal[:500])
plt.title("Target Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Jammer Signal
plt.subplot(4, 1, 2)
plt.plot(t[:500], jammer_signal[:500])
plt.title("Jammer Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Noise
plt.subplot(4, 1, 3)
plt.plot(t[:500], noise[:500])
plt.title("Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Mixed Signal
plt.subplot(4, 1, 4)
plt.plot(t[:500], mixed_signal[:500])
plt.title("Mixed Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()

# Frequency Analysis
plot_fft(target_signal, fs, "Target Signal")
plot_fft(jammer_signal, fs, "Jammer Signal")
plot_fft(mixed_signal, fs, "Mixed Signal")
