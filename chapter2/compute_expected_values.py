# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 2. Expected values and parameter estimation.

# Import libraries
import numpy as np

# Sample data (observations)
observations = [2, 4, 4, 4, 5, 5, 7, 9]

# Mean and variance as expected values ............................................................

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


# Mean and variance as momenta of distribution .................................................... 

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