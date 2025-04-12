#Section 1: Introduction to Matplotlib
import numpy as np
import matplotlib.pyplot as plt

def make_sine_wave(x, A, w):
    return A * np.sin(w * x)

x = np.linspace(0, 2 * np.pi, 1000)

amplitudes = [0.5, 1, 1.5, 2, 2.5]
frequencies = [1, 2, 3, 4, 5]

plt.figure(figsize=(10, 6))

line_styles = ['-', '--', '-.', ':', '-']  
for A, w, style in zip(amplitudes, frequencies, line_styles):
    y = make_sine_wave(x, A, w)
    plt.plot(x, y, linestyle=style, label=f"A={A}, w={w}")

plt.title("Sine Waves with Varying Amplitudes and Frequencies")
plt.xlabel("x")
plt.ylabel("y = A*sin(w*x)")
plt.legend()
plt.grid(True)
plt.show()


#Section 2: Data with Pandas
import pandas 
import matplotlib.pyplot as plt  

stars =pandas.read_csv("C:/Users/kaitl/python_decal/kaitlyn_decal/homework8/stars.csv")

print(stars.head())
print("Shape:", stars.shape)
print("Columns and dtypes:\n", stars.dtypes)


print("Average mass:", stars["Mass (M☉)"].mean())
print("Average temperature:", stars["Temperature (K)"].mean())
largest_radius_star = stars.loc[stars["Radius (R☉)"].idxmax()]
print("Star with largest radius:\n", largest_radius_star)
m_type_stars = stars[stars["Spectral_Type"].str.startswith("M")]
print("Number of M-type stars:", len(m_type_stars))

print("3 closest stars:\n", stars.sort_values("Distance (ly)").head(3))

m_type_stars.to_csv("m_type_stars.csv", index=False)

plt.figure(figsize=(8, 5))
plt.hist(stars["Temperature (K)"], bins=20, edgecolor='black')
plt.title("Temperature Distribution of Stars")
plt.xlabel("Temperature")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#Section 3: Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.scatterplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    style="sex",
    ax=axes[0]
)
axes[0].set_title("Bill Length vs. Bill Depth")
axes[0].set_xlabel("Bill Length (mm)")
axes[0].set_ylabel("Bill Depth (mm)")
axes[0].legend(title="Species")

sns.histplot(
    data=penguins,
    x="body_mass_g",
    bins=20,
    kde=True,
    ax=axes[1],
    color='skyblue'
)
axes[1].set_title("Body Mass Distribution")
axes[1].set_xlabel("Body Mass (g)")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()

