# Load necessary libraries
library(ggplot2)

# Set seed for reproducibility
set.seed(42)

# Central Limit Theorem (CLT) .....................................................................
cat("The central limit theorem (CLT)\n")

# Parameters
sample_size <- 30 # Size of each sample
# num_samples <- 10 # Number of samples for CLT
# num_samples <- 100 # Number of samples for CLT
num_samples <- 10000 # Number of samples for CLT

# True mean for comparison
dice_mean <- 3.5 # True mean for a six-sided die

# Dice roll sample means
dice_sample_means <- replicate(num_samples, mean(sample(1:6, sample_size, replace = TRUE)))

# Plotting CLT results
df <- data.frame(SampleMean = dice_sample_means)

# Plot sample mean distribution
ggplot(df, aes(x = SampleMean)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black", alpha = 0.7) +
  geom_density(color = "blue", size = 1) +
  geom_vline(xintercept = dice_mean, color = "red", linetype = "dashed", size = 1, label = "True Mean") +
  labs(
    title = "Central Limit Theorem - Dice Roll Sample Means",
    x = "Sample Mean of Dice Rolls",
    y = "Density"
  ) +
  theme_minimal()
