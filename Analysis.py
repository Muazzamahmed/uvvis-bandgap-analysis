import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load UV-Vis dataset
data = pd.read_csv("uvvis_data.csv")

# Extract columns
wavelength = data["Wavelength_nm"]
absorbance = data["Absorbance"]

# Convert wavelength to photon energy (eV)
hv = 1240 / wavelength

# Simplified absorption coefficient
alpha = absorbance * 100

# Tauc relation for direct bandgap
tauc = (alpha * hv)**2

# Plot absorbance spectrum
plt.figure()
plt.plot(wavelength, absorbance)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.title("UV-Vis Absorbance Spectrum")
plt.grid()

# Plot Tauc plot
plt.figure()
plt.plot(hv, tauc)

plt.xlabel("Photon Energy (eV)")
plt.ylabel(r"$(\alpha h\nu)^2$")
plt.title("Tauc Plot for Optical Bandgap Estimation")
plt.grid()

plt.show()
