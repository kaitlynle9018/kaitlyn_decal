import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import G  # Gravitational constant

# Load the composite dataset
data = pd.read_csv('PSCompPars.csv', low_memory=False)

# Filter for KOI-351 system
koi351 = data[data['pl_name'].str.contains('KOI-351', na=False)]

# Select relevant columns
koi351 = koi351[['pl_orbper', 'pl_bmasse', 'pl_rade']].dropna()
koi351.columns = ['Period', 'Mass', 'Radius']

# Check the data
print(koi351)
# Power-law model
def power_law(P, C, k):
    return C * P ** k

# Fit the model
popt, pcov = curve_fit(power_law, koi351['Period'], koi351['Mass'])

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(koi351['Period'], koi351['Mass'], label='Data', color='blue')
plt.plot(koi351['Period'], power_law(koi351['Period'], *popt), color='red', label=f'Fit: M = {popt[0]:.2f}P^{popt[1]:.2f}')
plt.xlabel("Orbital Period (days)")
plt.ylabel("Planet Mass (Earth Masses)")
plt.title("Mass-Period Relationship - KOI-351")
plt.legend()
plt.grid(True)
plt.show()
# Constants
M_star = 1.989e30  # kg (solar mass)

# Convert mass to kg and period to seconds
P_sec = koi351['Period'] * 24 * 3600
M_p = koi351['Mass'] * 5.972e24  # Earth mass to kg

# Solve for semi-major axis using rearranged Kepler’s Law
a_meters = ((G * (M_star + M_p) * P_sec**2) / (4 * np.pi**2)) ** (1/3)
a_au = a_meters / 1.496e11  # convert to AU

# Plotting semi-major axis vs period
plt.figure(figsize=(8, 5))
plt.scatter(koi351['Period'], a_au, color='green')
plt.xlabel("Orbital Period (days)")
plt.ylabel("Semi-Major Axis (AU)")
plt.title("Kepler's Law - KOI-351")
plt.grid(True)
plt.show()
# Linear model: y = mx + b
def linear_model(x, m, b):
    return m * x + b

# Fit
popt_linear, _ = curve_fit(linear_model, koi351['Radius'], koi351['Mass'])

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(koi351['Radius'], koi351['Mass'], label='Data')
plt.plot(koi351['Radius'], linear_model(koi351['Radius'], *popt_linear), color='orange', label=f'y = {popt_linear[0]:.2f}x + {popt_linear[1]:.2f}')
plt.xlabel("Radius (Earth Radii)")
plt.ylabel("Mass (Earth Masses)")
plt.title("Least Squares Fit: Mass vs Radius")
plt.legend()
plt.grid(True)
plt.show()
