# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 3 - Hypothesis testing.

# Import libraries
import numpy as np
from scipy.stats import ttest_1samp, t
import matplotlib.pyplot as plt

# Random seed
np.random.seed(42)

# Simulate 100 die rolls
rolls = np.random.randint(1, 7, size = 100)
# Simulate biased rools
probabilities = [0.1, 0.1, 0.2, 0.2, 0.1, 0.3]
rolls = np.random.choice([1, 2, 3, 4, 5, 6], size = 100, p = probabilities)

# Plot histogram of observations
plt.hist(rolls, bins = np.arange(1, 8) - 0.5, edgecolor = "black", rwidth = 0.8)
plt.xticks(range(1, 7))
plt.xlabel("Die face")
plt.ylabel("Frequency")
plt.title("Histogram of die rolls")
plt.show()

# Perform one-sided t-test
expected_mean = 3.5  # Assuming H0 (die is fair)
t_stat, p_value = ttest_1samp(rolls, popmean = expected_mean)
p_value_one_sided = p_value / 2 if t_stat > 0 else 1

# Plot t-distribution with critical value
df = len(rolls) - 1  # Degrees of freedom
critical_t = t.ppf(1 - 0.05, df)  # Critical t-value for 95% confidence, one-tailed

# Plot t-distribution
x = np.linspace(-4, 4, 1000)
y = t.pdf(x, df)
plt.plot(x, y, label = "t-Distribution")
plt.axvline(critical_t, color = "red", linestyle = "--", label = f"Critical t = {critical_t:.2f}")
plt.axvline(t_stat, color = "blue", linestyle = "--", label = f"Observed t = {t_stat:.2f}")
plt.fill_between(x, 0, y, where=(x >= critical_t), color = "red", alpha = 0.3, label = "Rejection Region")
plt.xlabel("t-value")
plt.ylabel("Probability density")
plt.title("T-distribution and critical value")
plt.legend()
plt.show()

# Print results
print(f"\nt-statistic: {t_stat:.4f}")
print(f"One-sided p-value: {p_value_one_sided:.4f}")
if p_value_one_sided < 0.05:
    print("The die is likely biased (reject null hypothesis).")
else:
    print("The die is not biased (fail to reject null hypothesis).\n")