# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Final assignment:
# Check if there is a significant difference between expected and observed choices.

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Simulate human-biased number choices
def simulate_human_choices(n_people):
    human_bias = [0.08, 0.12, 0.10, 0.10, 0.10, 0.10, 0.10, 0.15, 0.08, 0.07]  # Human bias distribution
    choices = np.random.choice(range(10), size = n_people * 3, p = human_bias)  # Each person picks 3 numbers
    return choices

# Simulate random choices
def simulate_random_choices(n_people):
    random_choices = np.random.randint(0, 10, size = n_people * 3)  # Uniform random distribution
    return random_choices

# Analyze frequencies
def analyze_frequencies(choices):
    frequencies = [np.sum(choices == i) for i in range(10)]  # Count occurrences of each number
    return np.array(frequencies)

# Main simulation
n_people = 20  # Number of participants
human_choices = simulate_human_choices(n_people)
random_choices = simulate_random_choices(n_people)

human_freq = analyze_frequencies(human_choices)
random_freq = analyze_frequencies(random_choices)

# Perform chi-square test
expected_freq = [n_people * 3 / 10] * 10  # Expected frequency for uniform distribution
chi2_stat, p_value = chisquare(human_freq, f_exp = expected_freq)

# Plot the results
x_labels = [str(i) for i in range(10)]
x = np.arange(len(x_labels))
plt.figure(figsize = (10, 6))
# Plot human (observed) choices
plt.bar(x - 0.2, human_freq, width = 0.4, label = "Human Choices", color = "skyblue")
# Plot random (expected) choices
plt.bar(x + 0.2, random_freq, width = 0.4, label = "Random Choices", color = "orange")
plt.axhline(y = n_people * 3 / 10, color = "gray", linestyle = "--", label = "Expected Uniform Frequency")
# Add lables and title
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.title("Distribution of Numbers: Human Choices vs Random Choices")
plt.xticks(x, x_labels)
plt.legend()
plt.show()

# Print results
print("Chi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: The observed distribution (human choices) significantly deviates from a uniform distribution.")
else:
    print("Conclusion: No significant deviation from a uniform distribution.")