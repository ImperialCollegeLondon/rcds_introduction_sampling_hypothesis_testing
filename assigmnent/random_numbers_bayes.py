# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Final assignment:
# Check if there is a significant difference between expected and observed choices.

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the prior (uniform distribution)
prior = np.ones(9) / 9  # Uniform prior: all numbers 1-9 have equal probability

# Step 2: Simulate the observed data (likelihood)
# For this example, let's assume the observed data is as follows:
# Number 1: chosen 40 times, Number 2: chosen 30 times, etc.
observed_data = [40, 30, 10, 5, 5, 3, 2, 3, 2]  # Number of times each number was chosen

# Step 3: Compute the likelihood based on observed data (no normalization needed)
# Here, we are directly using the observed frequencies as the likelihood.

# Step 4: Compute the posterior using Bayes' Theorem
# Posterior ∝ Likelihood * Prior
posterior = np.array(observed_data) * prior  # Element-wise multiplication

# Normalize the posterior (make sure it sums to 1)
posterior /= np.sum(posterior)

# Step 5: Plot the prior and posterior distributions
x = np.arange(1, 10)  # Numbers 1 to 9

plt.figure(figsize = (10, 6))
# Plot prior distribution
plt.bar(x - 0.2, prior, width=0.4, label="Prior", color="skyblue", alpha=0.7)
# Plot posterior distribution
plt.bar(x + 0.2, posterior, width=0.4, label="Posterior", color="orange", alpha=0.7)
# Add labels and title
plt.xlabel("Number")
plt.ylabel("Probability")
plt.title("Prior vs Posterior Distribution for Number Choices")
plt.xticks(x)
plt.legend()
plt.show()
