# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 2. Expected values and parameter estimation.

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up seaborn for prettier plots
sns.set(style = "whitegrid")

# Central Limit Theorem (CLT)
print("The central limit theorem (CLT)")

# We simulate 1,000 samples of size 30 for both dice rolls. Calculate and store the mean for each sample.
# The distribution of these sample means should approximate a normal distribution centered around the true mean.

# Parameters
sample_size = 30 # Size of each sample
# num_samples = 10 # Number of samples for CLT
# num_samples = 100 # Number of samples for CLT
num_samples = 1000 # Number of samples for CLT

# True means for comparison
dice_mean = 3.5 # True mean for a six-sided die

# Dice roll sample means
dice_sample_means = [np.mean(np.random.randint(1, 7, sample_size)) for _ in range(num_samples)]

# Plotting CLT results
plt.figure(figsize = (10, 5))

# Plot sample mean distribution
sns.histplot(dice_sample_means, kde = True, color = "skyblue", bins = 30)
plt.axvline(dice_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {dice_mean}")
plt.title("Central limit theorem - Dice roll sample means")
plt.xlabel("Sample mean of dice rolls")
plt.ylabel("Frequency")
plt.legend()
plt.show()
