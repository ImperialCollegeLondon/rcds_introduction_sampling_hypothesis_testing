# RCDS Introduction to Statistics and random sampling
# Jesus Urtasun Elizari - Imperial College London
# Chapter 1 - Random variables and probability distributions

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, ttest_1samp

def t_test(sample_data, pop_mean):
    """
    Perform a one-sample t-test.

    Args:
    - sample_data: List or array containing the sample data.
    - pop_mean: Population mean to test against.

    Returns:
    - A tuple containing the t-statistic and p-value.
    """
    n = len(sample_data)
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)  # Use Bessel's correction for sample standard deviation

    t_statistic = (sample_mean - pop_mean) / (sample_std / np.sqrt(n))
    p_value = 2 * (1 - t.cdf(np.abs(t_statistic), df=n - 1))  # two-tailed test

    return t_statistic, p_value

# Generate sample data
np.random.seed(42)  # for reproducibility
sample_data = np.random.normal(loc=90, scale=10, size=100)

# Plot sample data as histogram
plt.figure(figsize=(10, 5))
plt.hist(sample_data, bins=20, edgecolor='black', density=True)
plt.title('Sample Data Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Compute mean of sample data
sample_mean = np.mean(sample_data)
plt.axvline(x=sample_mean, color='r', linestyle='--', label=f'Sample Mean: {sample_mean:.2f}')
plt.show()


# Compute probability of the sample mean
t_statistic1, p_value1 = t_test(sample_data, pop_mean=90)
t_statistic2, p_value2 = ttest_1samp(sample_data, popmean=90)

# Print t-test results
print(f"Sample Mean: {sample_mean:.2f}")
print(f"t-statistic: {t_statistic1:.2f}, p-value: {p_value1:.4f}")
print(f"t-statistic: {t_statistic2:.2f}, p-value: {p_value2:.4f}")