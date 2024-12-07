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

# Perform two-sided t-test
expected_mean <- 3.5 # Assuming H0 (die is fair)
t_test <- t.test(rolls, mu = expected_mean) # Two-sided test

# Extract t-statistic and p-value
t_stat <- t_test$statistic
p_value <- t_test$p.value

# Degrees of freedom
df <- length(rolls) - 1

# Critical t-values for 95% confidence (two-tailed)
alpha <- 0.05
critical_t_left <- qt(alpha / 2, df)  # Lower critical value
critical_t_right <- qt(1 - alpha / 2, df)  # Upper critical value

# Generate data for t-distribution
x <- seq(-4, 4, length.out = 1000)
y <- dt(x, df)
t_dist_df <- data.frame(t_value = x, density = y)

# Plot t-distribution with critical and observed t-values
ggplot(t_dist_df, aes(x = t_value, y = density)) +
  geom_line(color = "black") +
  geom_vline(xintercept = critical_t_left, color = "red", linetype = "dashed", size = 1) +
  geom_vline(xintercept = critical_t_right, color = "red", linetype = "dashed", size = 1) +
  geom_vline(xintercept = t_stat, color = "blue", linetype = "dashed", size = 1) +
  # geom_area(data = subset(t_dist_df, t_value <= critical_t_left | t_value >= critical_t_right),
  #           aes(x = t_value, y = density), fill = "red", alpha = 0.3) +
  labs(title = "T-Distribution and Critical Values (Two-Sided Test)",
    x = "t-value",
    y = "Probability Density") +
  theme_minimal()

# Print results
cat(sprintf("Observed t-statistic: %.4f\n", t_stat))
cat(sprintf("Two-sided p-value: %.4f\n", p_value))
if (p_value < 0.05) {
  cat("The die is likely biased (reject null hypothesis).\n")
} else {
  cat("The die is not biased (fail to reject null hypothesis).\n")
}