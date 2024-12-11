## RCDS - Introduction to probability & statistical inference

### Dr. Jesús Urtasun Elizari

### Imperial College London - 2024 / 2025

<img src="/readme_figures/grad-school-logo.png">

## Chapter 2. Expected values & parameter estimation.

In this chapter we will describe parmeter estimation, mean and variance.
Then we will discuss the central limit theorem and the law of large numbers.

### Parameter estimation

Create a Python script for this exercise by running the following command in your terminal.

```bash

touch expected_values.py

```

Open the file with *VScode*.

```bash

code expected_values.py

```

Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

```

Mean and variance as expecet values:

```python

# Simulate observations
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Manual / numpy calculation of the mean (expected value)
mean_manual = sum(data) / len(data)
mean_np = np.mean(data)
print("\nMean as expected value (manual):", mean_manual)
print("Mean as expected value (numpy):", mean_np)

# Manual / numpy calculation of the variance (expected squared deviation)
squared_diffs = [(x - mean_manual) ** 2 for x in data]
variance_manual = sum(squared_diffs) / len(data)
variance_np = np.var(data, ddof = 0) # Population variance (ddof=0)
print("\nVariance as expected squared deviation (manual):", variance_manual)
print("Variance as expected squared deviation (numpy):", variance_np)

```

Median as middle point of an observation set
```python

# Manually compute the median
def manual_median(data):

    # Sort observation
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2  # Divide two numbers and truncate (round down) result to the nearest integer

    if n % 2 == 0:
        # Even number of elements: average the two middle values
        return (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        # Odd number of elements: return the middle value
        return sorted_data[middle]

# Manual / scipy calculation of the median
median_manual =  manual_median(data)
median_scipy = np.median(data)
print("\nMedian (manual):", median_manual)
print("Median (scipy):", median_scipy)

```

Mode as the most frequent value
```python

# Manually compute the mode
def manual_mode(data):

    # Create frequency vector
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    # Find argument that appears most
    max_count = max(frequency.values())
    modes = [key for key, count in frequency.items() if count == max_count]

    if len(modes) == 1:
        return modes[0] # Single mode
    else:
        return modes # Multiple modes or no clear mode


# Manual / scipy calculation of the mode
mode_manual = manual_mode(data)
mode_scipy = stats.mode(data, keepdims = True)
print("\nMode (manual):", mode_manual)
print("Mode (scipy):", mode_scipy.mode[0], "with frequency", mode_scipy.count[0])

```

### The central limit theorem:

Create a Python script for this exercise by running the following command in your terminal.

```bash

touch central_limit_theorem.py

```

Open the file with *VScode*.

```bash

code central_limit_theorem.py

```

Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

```

We simulate 1,000 samples of 30 dice rolls each. For each sample, we calculate the mean and store it.
We then plot the distribution of these sample means, and see how it converges to a normal distribution centered around the true mean.

```python

# Set up seaborn for prettier plots
sns.set(style = "whitegrid")

# Central Limit Theorem (CLT)
print("The central limit theorem (CLT)")

# We simulate 1,000 samples of size 30 for both dice rolls. Calculate and store the mean for each sample.
# The distribution of these sample means should approximate a normal distribution centered around the true mean.

# Parameters
sample_size = 30 # Size of each sample
# num_samples = 10 # Number of samples for CLT
# num_samples = 100 # Number of samples for CLT
num_samples = 1000 # Number of samples for CLT

# True means for comparison
dice_mean = 3.5 # True mean for a six-sided die

# Dice roll sample means
dice_sample_means = [np.mean(np.random.randint(1, 7, sample_size)) for _ in range(num_samples)]

# Plotting CLT results
plt.figure(figsize = (10, 5))

# Plot sample mean distribution
sns.histplot(dice_sample_means, kde = True, color = "skyblue", bins = 30)
plt.axvline(dice_mean, color = "red", linestyle = "dashed", linewidth = 2, label = f"True Mean = {dice_mean}")
plt.title("Central limit theorem - Dice roll sample means")
plt.xlabel("Sample mean of dice rolls")
plt.ylabel("Frequency")
plt.legend()
plt.show()

```

### The law of large numbers:

Create a Python script for this exercise by running the following command in your terminal.

```bash

touch law_large_numbers.py

```

Open the file with *VScode*.

```bash

code law_large_numbers.py

```

Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

```

We simulate 5,000 dice rolls. For each sample size from 1 to 5,000, we calculate the running mean.
We plot the running mean to show how it converges to the true mean, illustrating the LLN.

```python

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

```
