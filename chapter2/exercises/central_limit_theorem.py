# RCDS Introduction to Statistics and random sampling
# Jesus Urtasun Elizari - Imperial College London
# Chapter 1 - Random variables and probability distributions

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pdb

# Define parameters
population_distribution = np.random.randint(1, 7, 1000)  # Uniform distribution from 1 to 6 # bins = range(1, 8)
# population_distribution = np.random.binomial(n = 10, p = 0.5, size = 1000)
# population_distribution = np.random.poisson(lam = 5, size = 1000) # bins = range(-10, 10)
# population_distribution = np.random.normal(loc = 0, scale = 1, size = 1000) # bins = range(-10, 10)

# Define sample sizes for demonstration
sample_sizes = [10, 50, 200]

# Plot original population distribution
plt.hist(population_distribution, bins = range(1, 8), edgecolor = 'black', align = 'left', density = True)
plt.title('Original Population Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()

# Plot settings
plt.figure(figsize = (12, 8))

# Plot original population distribution
plt.subplot(2, 2, 1)
plt.hist(population_distribution, bins = range(1, 8), edgecolor = 'black', align = 'left', density = True)
plt.title('Original Population Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')

# Iterate over different sample sizes
for i, sample_size in enumerate(sample_sizes):

    # Get 
    sample_means = [np.mean(np.random.choice(population_distribution, sample_size)) for _ in range(1000)]
    
    # Plot sample mean distribution
    plt.subplot(2, 2, i+2)
    plt.hist(sample_means, bins=20, edgecolor='black', density=True)
    plt.title(f'Sample Mean Distribution (n={sample_size})')
    plt.xlabel('Mean')
    plt.ylabel('Probability')

plt.tight_layout()
plt.show()