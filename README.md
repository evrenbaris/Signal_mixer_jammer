# Signal Analysis with Target, Jammer, and Noise

## Overview

This project demonstrates signal processing techniques to analyze a mixed signal composed of a target signal, jammer signal, and noise. Using Python libraries such as NumPy, Matplotlib, and SciPy, the project visualizes the signals in both the time domain and frequency domain (via FFT).

---

## Features

- **Signal Composition**:
  - **Target Signal**: A sine wave with a frequency of 50 Hz.
  - **Jammer Signal**: A sine wave with a frequency of 80 Hz and a phase shift.
  - **Noise**: Gaussian random noise added to simulate real-world conditions.

- **Visualization**:
  - Time-domain plots of the target signal, jammer signal, noise, and the combined mixed signal.
  - Frequency-domain analysis using Fast Fourier Transform (FFT).

- **Frequency Analysis**:
  - Visualize frequency spectra of individual components and the mixed signal.

---

## Requirements

To run the code, you need the following Python libraries installed:
- `numpy`
- `matplotlib`
- `scipy`

You can install these dependencies using:
```bash
pip install numpy matplotlib scipy
