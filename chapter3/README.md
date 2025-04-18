## RCDS - Introduction to probability & statistical inference

### Dr. Jesús Urtasun Elizari

### Imperial College London - 2024 / 2025

<img src="/readme_figures/grad-school-logo.png">

## Chapter 3. Introduction to hypothesis testing.

In this chapter we will introduce hypothesis testing and statistical inference.
We will discuss the general approach to hypothesis testing, and show an example of a one-side and two-sided t-test.

### One-sided t-test

We will use a one sided t-test to check if a die is biased.
Create a Python script for this exercise by running the following command in your terminal.

```bash

touch t_test_1_sided.py

```

Open the file with *VScode*.

```bash

code t_test_1_sided.py

```

Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
from scipy.stats import ttest_1samp, t
import matplotlib.pyplot as plt

```

We will first simulate some rolls coming from a uniform distribution, and plot them as a histogram

```python

# Random seed
np.random.seed(42)

# Simulate 100 die rolls
rolls = np.random.randint(1, 7, size = 100)

# Plot histogram of observations
plt.hist(rolls, bins = np.arange(1, 8) - 0.5, edgecolor = "black", rwidth = 0.8)
plt.xticks(range(1, 7))
plt.xlabel("Die face")
plt.ylabel("Frequency")
plt.title("Histogram of die rolls")
plt.show()

```

Then we will compute the sample mean and compare it with the expected value if H0 is true, to build the t-statistic.
Since our alternative hypothtesis is p > 1/6 for some values, we will use a one-sided t test.

```python

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

```

Check what happens if we simulate a roll with biased values, 
by explicitely writing unequal probabilities for some of the faces.

```python

# Random seed
np.random.seed(42)

# # Simulate 100 die rolls
# rolls = np.random.randint(1, 7, size = 100)

# Simulate biased rools
probabilities = [0.1, 0.1, 0.2, 0.2, 0.1, 0.3]
rolls = np.random.choice([1, 2, 3, 4, 5, 6], size = 100, p = probabilities)

```

### Two-sided t-test

We will use a one sided t-test to check if a die is biased.
Create a Python script for this exercise by running the following command in your terminal.

```bash

touch t_test_2_sided.py

```

Open the file with *VScode*.

```bash

code t_test_2_sided.py

```

Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
from scipy.stats import ttest_1samp, t
import matplotlib.pyplot as plt

```

We will first simulate some rolls coming from a uniform distribution, and plot them as a histogram

```python

# Random seed
np.random.seed(42)

# Simulate 100 die rolls
rolls = np.random.randint(1, 7, size = 100)

# Plot histogram of observations
plt.hist(rolls, bins = np.arange(1, 8) - 0.5, edgecolor = "black", rwidth = 0.8)
plt.xticks(range(1, 7))
plt.xlabel("Die face")
plt.ylabel("Frequency")
plt.title("Histogram of die rolls")
plt.show()

```

Then we will compute the sample mean and compare it with the expected value if H0 is true, to build the t-statistic.
Since our alternative hypothtesis is p != 1/6 for some values, we will use a two-sided t test.

```python

# Perform two-sided t-test
expected_mean = 3.5  # Assuming H0 (die is fair)
t_stat, p_value = ttest_1samp(rolls, popmean = expected_mean)

# Plot t-distribution with critical values
df = len(rolls) - 1  # Degrees of freedom
alpha = 0.05  # Significance level
critical_t_left = t.ppf(alpha / 2, df)  # Lower critical t-value (negative tail)
critical_t_right = t.ppf(1 - alpha / 2, df)  # Upper critical t-value (positive tail)

# Plot t-distribution
x = np.linspace(-4, 4, 1000)
y = t.pdf(x, df)
plt.plot(x, y, label = "t-Distribution")
plt.axvline(critical_t_left, color = "red", linestyle = "--", label = f"Critical t = {critical_t_left:.2f}")
plt.axvline(critical_t_right, color = "red", linestyle = "--", label = f"Observed t = {critical_t_right:.2f}")
plt.axvline(t_stat, color = "blue", linestyle = "--", label = f"t-statistic = {t_stat:.2f}")
plt.fill_between(x, 0, y, where = (x <= critical_t_left) | (x >= critical_t_right), color = "red", alpha = 0.3, label = "Rejection Region")
plt.xlabel("t-value")
plt.ylabel("Probability density")
plt.title("T-distribution and critical values (two-sided test)")
plt.legend()
plt.show()

# Print results
print(f"t-statistic: {t_stat:.4f}")
print(f"Two-sided p-value: {p_value:.4f}")
if p_value < 0.05:
    print("The die is likely biased (reject null hypothesis).")
else:
    print("The die is not biased (fail to reject null hypothesis).")

```

Check what happens if we simulate a roll with biased values, 
by explicitely writing unequal probabilities for some of the faces.

```python

# Random seed
np.random.seed(42)

# # Simulate 100 die rolls
# rolls = np.random.randint(1, 7, size = 100)

# Simulate biased rools
probabilities = [0.1, 0.1, 0.2, 0.2, 0.1, 0.3]
rolls = np.random.choice([1, 2, 3, 4, 5, 6], size = 100, p = probabilities)

```