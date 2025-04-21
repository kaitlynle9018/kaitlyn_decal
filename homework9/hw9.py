
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from astropy.table import Table

#Section 1.1
df = pd.read_csv('C:/Users/kaitl/python_decal/kaitlyn_decal/homework9/GlobalLandTemperaturesByState.csv')
df = df[['dt', 'AverageTemperature', 'State']]
df['dt'] = pd.to_datetime(df['dt'])

df = df[df['dt'].dt.year > 2000]
df = df[df['State'].isin(['Wyoming', 'Nebraska', 'South Dakota'])]

print(df.shape)  

#Section 1.2 
avg_temp_df = df.groupby('dt')['AverageTemperature'].mean().reset_index()
avg_temp_df.columns = ['date', 'avg_temp']

#Section 1.3 
plt.figure(figsize=(12, 5))
plt.plot(avg_temp_df['date'], avg_temp_df['avg_temp'], label='Avg Temp')
plt.xlabel('Date')
plt.ylabel('Avg Temperature (°C)')
plt.title('Average Temperature for WY, NE, SD (2000+)')
plt.legend()
plt.grid(True)
plt.show()

#Section 1.4
avg_temp_df['date_num'] = avg_temp_df['date'].apply(lambda x: x.toordinal())

#Section 1.5 
def model(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

x_data = avg_temp_df['date_num'].values
y_data = avg_temp_df['avg_temp'].values

# Initial guesses:
# a = amplitude ~ 10
# b = frequency ~ 2π/year => 2π/(365.25) => ~0.017
# c = phase shift ~ 0
# d = vertical shift ~ mean temperature
initial_guess = [10, 0.017, 0, np.mean(y_data)]

#Section 1.6
popt, pcov = curve_fit(model, x_data, y_data, p0=initial_guess)

#Section 1.7
plt.figure(figsize=(12, 5))
plt.plot(avg_temp_df['date'], y_data, label='Avg Temp')
plt.plot(avg_temp_df['date'], model(x_data, *popt), label='Fitted Curve', color='red')
plt.xlabel('Date')
plt.ylabel('Avg Temperature (°C)')
plt.title('Curve Fit: Avg Temp for WY, NE, SD')
plt.legend()
plt.grid(True)
plt.show()

#Section 1.8 and 1.9
errors = np.sqrt(np.diag(pcov))
params = ['a', 'b', 'c', 'd']

for i in range(4):
    print(f'{params[i]} = {popt[i]:.4f} ± {errors[i]:.4f}')

# Final equation:
print(f'\nFinal Equation:\nT(x) = {popt[0]:.4f} * sin({popt[1]:.6f} * x + {popt[2]:.4f}) + {popt[3]:.4f}')

#Section 1.10 
table = Table.read('C:/Users/kaitl/python_decal/kaitlyn_decal/homework9/global_SF6_MM.dat', format='ascii.commented_header')
df_gas = table.to_pandas()

df_gas = df_gas[['year', 'mean', 'sd']]
df_gas.columns = ['year', 'mean_conc', 'sd_conc']

plt.errorbar(df_gas['year'], df_gas['mean_conc'], yerr=df_gas['sd_conc'], fmt='o', label='SF6 Concentration')
plt.xlabel('Year')
plt.ylabel('Mean Global SF6 (ppt)')
plt.title('Global SF6 Concentration Over Time')
plt.grid(True)
plt.legend()
plt.show()

def linear_model(x, m, b):
    return m * x + b

popt_lin, pcov_lin = curve_fit(linear_model, df_gas['year'], df_gas['mean_conc'], sigma=df_gas['sd_conc'], absolute_sigma=True)
errors_lin = np.sqrt(np.diag(pcov_lin))

residuals = df_gas['mean_conc'] - linear_model(df_gas['year'], *popt_lin)
chi_squared = np.sum((residuals / df_gas['sd_conc'])**2)
dof = len(df_gas) - len(popt_lin)
reduced_chi_squared = chi_squared / dof

print(f'm = {popt_lin[0]:.4f} ± {errors_lin[0]:.4f}')
print(f'b = {popt_lin[1]:.4f} ± {errors_lin[1]:.4f}')
print(f'\nFinal Equation: y = {popt_lin[0]:.4f}x + {popt_lin[1]:.4f}')
print(f'Reduced Chi-squared = {reduced_chi_squared:.4f}')

