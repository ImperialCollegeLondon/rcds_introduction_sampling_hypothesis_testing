# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 2. Expected values and parameter estimation.

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up seaborn for prettier plots
sns.set(style = "whitegrid")

# Central Limit Theorem (CLT) .....................................................................
print("The central limit theorem (CLT)")

# We simulate 1,000 samples of size 30 for both dice rolls and waiting times
# For each sample, we calculate the mean and store it.
# We then plot the distribution of these sample means. 
# According to the CLT, these distributions should approximate a normal distribution centered around the true mean.

# Parameters
sample_size = 30 # Size of each sample
# num_samples = 10 # Number of samples for CLT
# num_samples = 100 # Number of samples for CLT
num_samples = 1000 # Number of samples for CLT

# True means for comparison
dice_mean = 3.5 # True mean for a six-sided die
waiting_times = np.array([1, 2, 2, 3, 5, 10, 15, 20, 30, 60])
waiting_time_mean = np.mean(waiting_times) # True mean for waiting times

# Dice roll sample means
dice_sample_means = [np.mean(np.random.randint(1, 7, sample_size)) for _ in range(num_samples)]

# Skewed waiting time sample means
waiting_time_sample_means = [np.mean(np.random.choice(waiting_times, sample_size)) for _ in range(num_samples)]

# Plotting CLT results
plt.figure(figsize = (14, 6))

# Dice CLT Plot
plt.subplot(1, 2, 1)
sns.histplot(dice_sample_means, kde = True, color = "skyblue", bins = 30)
plt.axvline(dice_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {dice_mean}")
plt.title("Central limit theorem - Dice roll sample means")
plt.xlabel("Sample mean of dice rolls")
plt.ylabel("Frequency")
plt.legend()

# Waiting Time CLT Plot
plt.subplot(1, 2, 2)
sns.histplot(waiting_time_sample_means, kde = True, color = "salmon", bins = 30)
plt.axvline(waiting_time_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {waiting_time_mean:.2f}")
plt.title("Central limit theorem - Waiting time sample seans")
plt.xlabel("Sample mean of waiting times")
plt.ylabel("Frequency")
plt.legend()

# Combine plots
plt.tight_layout()
plt.show()


### Law of large numbers (LLN) ....................................................................
print("The law of large numbers (LLN)")

# Parameters
# num_samples = 50 # Number of samples for LLN
# num_samples = 500 # Number of samples for LLN
num_samples = 5000 # Number of samples for LLN

# We simulate 5,000 rolls for the dice and 5,000 samples from the waiting times.
# For each sample size from 1 to 5,000, we calculate the running mean.
# We plot the running mean to show how it converges to the true mean, illustrating the LLN.

# Dice Running Mean
dice_rolls = np.random.randint(1, 7, num_samples)  # Simulate 5000 dice rolls
dice_running_mean = np.cumsum(dice_rolls) / np.arange(1, num_samples + 1)

# Waiting Time Running Mean
waiting_time_rolls = np.random.choice(waiting_times, num_samples)  # Simulate 5000 waiting times
waiting_time_running_mean = np.cumsum(waiting_time_rolls) / np.arange(1, num_samples + 1)

# Plotting LLN results
plt.figure(figsize = (14, 6))

# Dice LLN Plot
plt.subplot(1, 2, 1)
plt.plot(dice_running_mean, color = "skyblue", label = "Running Mean")
plt.axhline(dice_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {dice_mean}")
plt.title("Law of large numbers - Dice roll running mean")
plt.xlabel("Number of rolls")
plt.ylabel("Mean of dice rolls")
plt.legend()

# Waiting Time LLN Plot
plt.subplot(1, 2, 2)
plt.plot(waiting_time_running_mean, color = "salmon", label = "Running Mean")
plt.axhline(waiting_time_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {waiting_time_mean:.2f}")
plt.title("Law of large numbers - Waiting time running mean")
plt.xlabel("Number of samples")
plt.ylabel("Mean of waiting times")
plt.legend()

plt.tight_layout()
plt.show()