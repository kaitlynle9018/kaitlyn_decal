import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize as fit

file_path = "C:/Users/kaitl/python_decal/kaitlyn_decal/final_project/PSCompPars_KOI_systems.csv"


df = pd.read_csv(file_path, comment='#', on_bad_lines='skip')

koi = df[df['pl_name'].str.contains('KOI', na=False)]

koi = koi[['pl_name', 'pl_orbper', 'pl_bmasse', 'pl_rade']].dropna()
koi.columns = ['Name', 'Period', 'Mass', 'Radius']

# Plot 1: Mass vs period 
koi_filtered = koi[(koi['Mass'] > 1) & (koi['Mass'] < 100) & (koi['Period'] > 0)]
#plt.figure(figsize=(8, 5))
#plt.scatter(koi_filtered['Period'], koi_filtered['Mass'], alpha=0.5, color='teal')
#plt.xlabel('Orbital Period (days)')
#plt.ylabel('Mass (Earth Masses)')
#plt.title('KOI Planets: Mass vs Period')
#plt.grid(True)
#plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(koi_filtered['Period'], koi_filtered['Mass'], alpha=0.5, label='Filtered KOI Data', color='gray')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Earth Masses)')
plt.title('KOI Planets: Mass vs Period')
plt.legend()
plt.grid(True, which='both')
plt.show()


# Plot 2: Period vs Radius (log scale) 
plt.figure(figsize=(8, 5))
plt.scatter(koi['Period'], koi['Radius'], alpha=0.5, color='indigo')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Planet Radius (Earth Radii)')
plt.title('KOI Planets: Period vs Radius')
plt.grid(True, which='both')
plt.show()

#3.1 plot: mass v period
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit

koi_filtered = koi[(koi['Mass'] > 1) & (koi['Mass'] < 100) & (koi['Period'] > 0)]

def power_law(x, C, k):
    return C * x**k

popt, pcov = fit(power_law, koi_filtered['Period'], koi_filtered['Mass'], p0=[1, 0.5])

C_fit, k_fit = popt
print(f"Fitted Power Law: M = {C_fit:.2f} * P^{k_fit:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(koi_filtered['Period'], koi_filtered['Mass'], alpha=0.5, label='Filtered KOI Data', color='gray')

P_plot = np.logspace(np.log10(koi_filtered['Period'].min()), np.log10(koi_filtered['Period'].max()), 500)

plt.plot(P_plot, power_law(P_plot, *popt), color='green', label=f'Fit: M = {C_fit:.2f}P^{k_fit:.2f}', lw=2)

# Log scales
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Earth Masses)')
plt.title('Mass-Period Power Law Fit (KOI Filtered)')
plt.legend()
plt.grid(True, which='both')
plt.show()

#Residual for Mass and Period
# Actual values
X = koi_filtered['Period']
Y = koi_filtered['Mass']

# Predicted values from model
Y_pred = power_law(X, *popt)

# Residuals
residuals = Y - Y_pred

# Plot residuals
plt.figure(figsize=(10, 5))
plt.scatter(X, residuals, color='gray', alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.xscale('log')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Residuals (Mass - Predicted Mass)')
plt.title('Residuals of Mass vs Period Fit')
plt.grid(True, which='both')
plt.show()

# Plot 3: Mass-Period Power Law Fit
#import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit as fit

#def power_law(x, C, k):
    #return C * (x ** k)

# Initial guess
#p100 = [1,0.5]

# Fit model
#popt, cov = fit(power_law, koi['Period'], koi['Mass'], p0=p100)
#print(popt)


# Plot
#plt.figure(figsize=(8, 5))
#plt.scatter(koi['Period'], koi['Mass'], alpha=0.4, label='Data', color='gray')
#plt.plot(koi['Period'], power_law(koi['Period'], *popt), color='crimson',
 #        label=f'Fit: M = {popt[0]:.2f}P^{popt[1]:.2f}')
#plt.xscale('log')
#plt.yscale('log')
#plt.xlabel('Orbital Period (days)')
#plt.ylabel('Mass (Earth Masses)')
#plt.title('Mass-Period Power Law Fit (KOI Systems)')
#plt.legend()
#plt.grid(True, which='both')
#plt.show()

#plot 5: Period vs Radius Relationship
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Filter for positive period and radius values
koi_filtered_PR = koi[(koi['Radius'] > 0) & (koi['Period'] > 0)]

def power_law_PR(x, C, k):
    return C * x**k


popt_PR, pcov_PR = curve_fit(power_law_PR, koi_filtered_PR['Period'], koi_filtered_PR['Radius'], p0=[1, 0.5])

# best-fit parameters
C_PR, k_PR = popt_PR
print(f"Fitted Period-Radius Relationship: R = {C_PR:.2f} * P^{k_PR:.2f}")


plt.figure(figsize=(10, 6))
plt.scatter(koi_filtered_PR['Period'], koi_filtered_PR['Radius'], alpha=0.5, color='purple', label='Data')


P_plot = np.logspace(np.log10(koi_filtered_PR['Period'].min()), np.log10(koi_filtered_PR['Period'].max()), 500)


plt.plot(P_plot, power_law_PR(P_plot, *popt_PR), color='orange', lw=2,
         label=f'Fit: R = {C_PR:.2f}P^{k_PR:.2f}')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Planet Radius (Earth Radii)')
plt.title('Period vs Radius Power Law Fit (KOI Systems)')
plt.legend()
plt.grid(True, which='both')
plt.show()
#Residuals for Period and Radius
X = koi_filtered_PR['Period']
Y = koi_filtered_PR['Radius']
Y_pred = power_law_PR(X, *popt_PR)
residuals = Y - Y_pred

plt.figure(figsize=(10, 5))
plt.scatter(X, residuals, color='purple', alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.xscale('log')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Residuals (Radius - Predicted Radius)')
plt.title('Residuals of Radius vs Period Fit')
plt.grid(True, which='both')
plt.show()

# Plot 4: Heatmap of Correlations
#plt.figure(figsize=(6, 5))
#corr = koi[['Period', 'Mass', 'Radius']].corr()
#sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
#plt.title('Correlation Matrix of KOI Planet Parameters')
#plt.show()
