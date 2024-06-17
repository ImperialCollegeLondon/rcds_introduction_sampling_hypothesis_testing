# RCDS Introduction to Statistics and random sampling
# Jesus Urtasun Elizari - Imperial College London
# Chapter 3 - Hypothesis testing

# Import libraries
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Function plotting histogram
def plot_histogram(die_rolls):
    """
    Plot a histogram of the die rolls.
    
    Parameters:
    die_rolls (list or array): The observed rolls of the die.
    """
    plt.hist(die_rolls, bins=np.arange(1, 8) - 0.5, edgecolor='black', rwidth=0.8)
    plt.xticks(range(1, 7))
    plt.xlabel('Die Roll')
    plt.ylabel('Frequency')
    plt.title('Histogram of Die Rolls')
    plt.show()

# Function computing one-sample t-test
def t_test_die_rolls(die_rolls):
    """
    Perform a one-sample t-test to check if the die is fair.
    
    Parameters:
    die_rolls (list or array): The observed rolls of the die.
    
    Returns:
    t_statistic (float): The t-statistic value.
    p_value (float): The p-value of the t-test.
    """
    # Calculate the observed mean
    observed_mean = np.mean(die_rolls)
    
    # Expected mean for a fair die
    expected_mean = 3.5
    
    # Perform the one-sample t-test
    t_statistic, p_value = stats.ttest_1samp(die_rolls, expected_mean)
    
    return t_statistic, p_value

# Formulate null and alternative hypothesis
# H0 (...)
# H1 (...)

# Collect data
die_rolls = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

# Plot the histogram
plot_histogram(die_rolls)

# Perform the t-test
t_statistic, p_value = t_test_die_rolls(die_rolls)

# Print results
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("The die is likely loaded (reject the null hypothesis).")
else:
    print("The die is likely fair (fail to reject the null hypothesis).")