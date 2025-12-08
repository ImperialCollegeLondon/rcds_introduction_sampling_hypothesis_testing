# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 2. Expected values and parameter estimation.

# Import libraries
import numpy as np
from scipy import stats

# Simulate observations
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Manual / numpy calculation of the mean (expected value)
mean_manual = sum(data) / len(data)
mean_np = np.mean(data)
print("\nSample mean (manual):", mean_manual)
print("Sample mean (numpy):", mean_np)

# Manual / numpy calculation of the variance (expected squared deviation)
squared_diffs = [(x - mean_manual) ** 2 for x in data]
variance_manual = sum(squared_diffs) / len(data)
variance_np = np.var(data, ddof = 0) # Population variance (ddof=0)
print("\nSample variance (manual):", variance_manual)
print("Sample variance (numpy):", variance_np)

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