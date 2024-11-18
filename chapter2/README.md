## RCDS - Introduction to probability & statistical inference

### Dr. Jesús Urtasun Elizari

### Imperial College London - 2024 / 2025

<img src="/readme_figures/grad-school-logo.png">

## Chapter 2. Expected values & parameter estimation.

In this chapter we will describe parmeter estimation, mean and variance.
Then we will discuss the central limit theorem and the law of large numbers.
Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
from math import comb, exp, factorial, erf, sqrt
from scipy import stats
import matplotlib.pyplot as plt

```

### Parameter estimation

Mean and variance as expecet values:

```python

# Manual / numpy calculation of the mean (expected value)
mean_observations_manual = sum(observations) / len(observations)
mean_observations_np = np.mean(observations)
print("\nMean as expected value (numpy):", mean_observations_np)
print("Mean as expected value (manual):", mean_observations_manual)

# Manal / numpy calculation of the Variance (expected squared deviation)
variance_observations_np = np.var(observations, ddof = 0) # Population variance (ddof=0)
squared_diffs = [(x - mean_observations_manual) ** 2 for x in observations]
variance_observations_manual = sum(squared_diffs) / len(observations)
print("Variance as expected squared deviation (numpy):", variance_observations_np)
print("Variance as expected squared deviation (manual):", variance_observations_manual)

```

Mean and variance as momenta of distribution:

```python

# Simulate a probability distribution (example with outcomes and probabilities)
# Suppose we have a random variable X with possible values and their probabilities:
values = np.array([2, 4, 5, 7, 9]) # Possible outcomes
probabilities = np.array([0.1, 0.3, 0.2, 0.2, 0.2]) # Corresponding probabilities (must sum to 1)

# Mean as first moment of distribution
mean_distribution = np.sum(values * probabilities)
print("\nMean as first moment of the distribution:", mean_distribution)

# Variance as second moment of distribution
variance_distribution = np.sum((values - mean_distribution)**2 * probabilities)
print("Variance as second moment of the distribution:", variance_distribution)

```

### The law of large numbers and the central limit theorem

The central limit theorem:

```python

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

```

The law of large numbers:

```python

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

```