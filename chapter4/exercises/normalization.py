# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 3 - Hypothesis testing.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# # Simulate three datasets
# np.random.seed(42)
# data1 = np.random.randint(10, 100, size=(100, 3))  # Uniformly distributed integers between 10 and 100
# data2 = np.random.randn(100, 3) * 10 + 50  # Normally distributed data with mean=50, std=10
# data3 = np.random.exponential(scale=2.0, size=(100, 3))  # Exponentially distributed data with scale=2.0

# # Convert to dataframe
# df1 = pd.DataFrame(data1, columns=['Feature1', 'Feature2', 'Feature3'])
# df2 = pd.DataFrame(data2, columns=['Feature1', 'Feature2', 'Feature3'])
# df3 = pd.DataFrame(data3, columns=['Feature1', 'Feature2', 'Feature3'])

# # Save data as csv
# df1.to_csv('00_data/dataset1.csv', index=False)
# df2.to_csv('00_data/dataset2.csv', index=False)
# df3.to_csv('00_data/dataset3.csv', index=False)

# # Plot histograms
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# colors = ['#1f77b4', '#76c7c0', '#4c72b0']  # Different shades of bluish colors
# titles = ["Uniform Distribution (Dataset 1)", "Normal Distribution (Dataset 2)", "Exponential Distribution (Dataset 3)"]
# # Axes for each dataset
# for i, df in enumerate([df1, df2, df3]):
#     axes[i].hist(df.values.flatten(), bins=20, color=colors[i], alpha=0.7, edgecolor='black')
#     axes[i].set_title(titles[i])
#     axes[i].grid(axis='y', linestyle='--', alpha=0.7)
#     axes[i].set_xlabel("Value")
#     axes[i].set_ylabel("Frequency")

# plt.tight_layout()
# plt.savefig("histograms.png", dpi=300)
# plt.show()
# print("Datasets and histograms have been saved.")

# Load datasets from CSV files
# Replace 'dataset1.csv', 'dataset2.csv', and 'dataset3.csv' with your actual file paths
dataset1 = pd.read_csv('dataset1.csv').values.flatten()  # Assuming the CSV has a single column
dataset2 = pd.read_csv('dataset2.csv').values.flatten()  # Assuming the CSV has a single column
dataset3 = pd.read_csv('dataset3.csv').values.flatten()  # Assuming the CSV has a single column

# Function to plot histograms
def plot_histogram(data, title, bins=30):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Plot original datasets
plot_histogram(dataset1, 'Original Dataset 1')
plot_histogram(dataset2, 'Original Dataset 2')
plot_histogram(dataset3, 'Original Dataset 3')

# Normalization

# Min-Max Normalization for Dataset 1
scaler_minmax = MinMaxScaler()
dataset1_normalized = scaler_minmax.fit_transform(dataset1.reshape(-1, 1)).flatten()

# Z-score Normalization for Dataset 2
scaler_zscore = StandardScaler()
dataset2_normalized = scaler_zscore.fit_transform(dataset2.reshape(-1, 1)).flatten()

# Log Normalization for Dataset 3
dataset3_normalized = np.log1p(dataset3)  # Using log1p to handle zero values

# Plot normalized datasets
plot_histogram(dataset1_normalized, 'Min-Max Normalized Dataset 1')
plot_histogram(dataset2_normalized, 'Z-score Normalized Dataset 2')
plot_histogram(dataset3_normalized, 'Log Normalized Dataset 3')
