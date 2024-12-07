# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 2. Expected values and parameter estimation.

# Sample data (observations)
observations <- c(2, 4, 4, 4, 5, 5, 7, 9)

# Mean and variance as expected values ............................................................

# Manual calculation of the mean (expected value)
mean_observations_manual <- sum(observations) / length(observations)
mean_observations_r <- mean(observations)
cat("\nMean as expected value (R built-in):", mean_observations_r, "\n")
cat("Mean as expected value (manual):", mean_observations_manual, "\n")

# Manual calculation of the variance (expected squared deviation)
variance_observations_r <- var(observations) * (length(observations) - 1) / length(observations) # Population variance
squared_diffs <- (observations - mean_observations_manual)^2
variance_observations_manual <- sum(squared_diffs) / length(observations)
cat("Variance as expected squared deviation (R built-in):", variance_observations_r, "\n")
cat("Variance as expected squared deviation (manual):", variance_observations_manual, "\n")

# Mean and variance as moments of a distribution .................................................... 

# Simulate a probability distribution (example with outcomes and probabilities)
# Suppose we have a random variable X with possible values and their probabilities:
values <- c(2, 4, 5, 7, 9) # Possible outcomes
probabilities <- c(0.1, 0.3, 0.2, 0.2, 0.2) # Corresponding probabilities (must sum to 1)

# Mean as first moment of the distribution
mean_distribution <- sum(values * probabilities)
cat("\nMean as first moment of the distribution:", mean_distribution, "\n")

# Variance as second moment of the distribution
variance_distribution <- sum((values - mean_distribution)^2 * probabilities)
cat("Variance as second moment of the distribution:", variance_distribution, "\n")
