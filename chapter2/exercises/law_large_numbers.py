# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 2. Expected values and parameter estimation.

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up seaborn for prettier plots
sns.set(style = "whitegrid")

# The law of large numbers (LLN)
print("The law of large numbers (LLN)")

# Simulate 5,000 dice rolls. Calculate and store the mean for all samples.
# The running mean, as function of number of samples, should converges to the true mean.

# True means for comparison
dice_mean = 3.5 # True mean for a six-sided die

# Parameters
# num_samples = 50 # Number of samples for LLN
# num_samples = 500 # Number of samples for LLN
num_samples = 5000 # Number of samples for LLN

# Dice Running Mean
dice_rolls = np.random.randint(1, 7, num_samples)  # Simulate 5000 dice rolls
dice_running_mean = np.cumsum(dice_rolls) / np.arange(1, num_samples + 1)

# Plotting LLN results
plt.figure(figsize = (10, 5))

# Plot running mean
plt.plot(dice_running_mean, color = "skyblue", label = "Running Mean")
plt.axhline(dice_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {dice_mean}")
plt.title("Law of large numbers - Dice roll running mean")
plt.xlabel("Number of rolls")
plt.ylabel("Mean of dice rolls")
plt.legend()
plt.show()
