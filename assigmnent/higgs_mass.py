# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Final assignment:
# Check if there is a significant difference between various measurements of the Higgs boson mass.

# Import libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Theoretical value of the Higgs boson mass
theoretical_mass = 125.4 # (in GeV)
alpha = 0.05  # Significance level

# Read input data
cms_data = pd.read_csv("data/higgs_mass_cms.csv")
atlas_data = pd.read_csv("data/higgs_mass_atlas.csv")
lhcb_data = pd.read_csv("data/higgs_mass_lhcb.csv")

# Extract mass data as numpy arrays
cms_measurements = cms_data["Higgs_Mass_CMS"].values
atlas_measurements = atlas_data["Higgs_Mass_ATLAS"].values
lhcb_measurements = lhcb_data["Higgs_Mass_LHCb"].values

# Calculate mean and variance for each dataset
cms_mean, cms_variance = np.mean(cms_measurements), np.var(cms_measurements)
atlas_mean, atlas_variance = np.mean(atlas_measurements), np.var(atlas_measurements)
lhcb_mean, lhcb_variance = np.mean(lhcb_measurements), np.var(lhcb_measurements)

# Plot histograms
plt.figure(figsize = (15, 5))

# CMS Histogram
plt.subplot(1, 3, 1)
plt.hist(cms_measurements, bins = 30, color = "skyblue", edgecolor = "black", alpha = 0.7)
plt.axvline(cms_mean, color = "red", linestyle = "dashed", linewidth = 1)
plt.title(f"CMS measurements\nMean = {cms_mean:.2f} GeV, variance = {cms_variance:.2f}")
plt.xlabel("Higgs mass (GeV)")
plt.ylabel("Frequency")

# ATLAS Histogram
plt.subplot(1, 3, 2)
plt.hist(atlas_measurements, bins = 30, color = "lightgreen", edgecolor = "black", alpha = 0.7)
plt.axvline(atlas_mean, color = "red", linestyle = "dashed", linewidth = 1)
plt.title(f"ATLAS measurements\nMean = {atlas_mean:.2f} GeV, variance = {atlas_variance:.2f}")
plt.xlabel("Higgs mass (GeV)")
plt.ylabel("Frequency")

# LHCb Histogram
plt.subplot(1, 3, 3)
plt.hist(lhcb_measurements, bins = 30, color = "lightcoral", edgecolor = "black", alpha = 0.7)
plt.axvline(lhcb_mean, color = "red", linestyle = "dashed", linewidth = 1)
plt.title(f"LHCb measurements\nMean = {lhcb_mean:.2f} GeV, variance = {lhcb_variance:.2f}")
plt.xlabel("Higgs mass (GeV)")
plt.ylabel("Frequency")

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Perform one-sample t-tests against the theoretical Higgs mass
t_stat_cms, p_value_cms = stats.ttest_1samp(cms_measurements, theoretical_mass)
t_stat_atlas, p_value_atlas = stats.ttest_1samp(atlas_measurements, theoretical_mass)
t_stat_lhcb, p_value_lhcb = stats.ttest_1samp(lhcb_measurements, theoretical_mass)

# Display the results
print(f"\nCMS t-test: t-statistic = {t_stat_cms:.4f}, p-value = {p_value_cms:.4e}")
print(f"ATLAS t-test: t-statistic = {t_stat_atlas:.4f}, p-value = {p_value_atlas:.4e}")
print(f"LHCb t-test: t-statistic = {t_stat_lhcb:.4f}, p-value = {p_value_lhcb:.4e}")

# Interpret the results
if p_value_cms < alpha:
    print("\nCMS data is significantly different from the theoretical value.")
else:
    print("\nCMS data is not significantly different from the theoretical value.")

if p_value_atlas < alpha:
    print("ATLAS data is significantly different from the theoretical value.")
else:
    print("ATLAS data is not significantly different from the theoretical value.")

if p_value_lhcb < alpha:
    print("LHCb data is significantly different from the theoretical value.")
else:
    print("LHCb data is not significantly different from the theoretical value.")