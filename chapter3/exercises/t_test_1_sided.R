# Load necessary libraries
library(ggplot2)

# Set seed for reproducibility
set.seed(42)

# Simulate 100 die rolls
# rolls <- sample(1:6, size = 100, replace = TRUE) # Fair dice rolls
# Simulate biased rolls
probabilities <- c(0.1, 0.1, 0.2, 0.2, 0.1, 0.3)
rolls <- sample(1:6, size = 100, replace = TRUE, prob = probabilities)

# Plot histogram of observations
rolls_df <- data.frame(DieFace = factor(rolls, levels = 1:6))
ggplot(rolls_df, aes(x = DieFace)) +
  geom_bar(fill = "skyblue", color = "black", width = 0.7) +
  labs(title = "Histogram of Die Rolls",
    x = "Die Face",
    y = "Frequency") +
  theme_minimal()

# Perform one-sided t-test
expected_mean <- 3.5 # Assuming H0 (die is fair)
t_test <- t.test(rolls, mu = expected_mean, alternative = "greater") # One-sided test

# Extract t-statistic and p-value
t_stat <- t_test$statistic
p_value_one_sided <- t_test$p.value

# Degrees of freedom
df <- length(rolls) - 1

# Critical t-value for 95% confidence (one-tailed)
critical_t <- qt(0.95, df)

# Generate data for t-distribution
x <- seq(-4, 4, length.out = 1000)
y <- dt(x, df)
t_dist_df <- data.frame(t_value = x, density = y)

# Plot t-distribution with critical and observed t-values
ggplot(t_dist_df, aes(x = t_value, y = density)) +
  geom_line(color = "black") +
  geom_vline(xintercept = critical_t, color = "red", linetype = "dashed", size = 1, label = "Critical t") +
  geom_vline(xintercept = t_stat, color = "blue", linetype = "dashed", size = 1, label = "Observed t") +
  geom_area(data = subset(t_dist_df, t_value >= critical_t), aes(x = t_value, y = density), fill = "red", alpha = 0.3) +
  labs(title = "T-Distribution and Critical Value",
    x = "t-value",
    y = "Probability Density") +
  theme_minimal()

# Print results
cat(sprintf("\nObserved t-statistic: %.4f\n", t_stat))
cat(sprintf("One-sided p-value: %.4f\n", p_value_one_sided))
if (p_value_one_sided < 0.05) {
  cat("The die is likely biased (reject null hypothesis).\n")
} else {
  cat("The die is not biased (fail to reject null hypothesis).\n")
}
