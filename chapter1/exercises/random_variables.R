# RCDS Introduction to probability and statistical inference.
# Jesús Urtasun Elizari. ICL 2024 / 2025.
# Chapter 1. Introduction to probability and random events.

# Load necessary libraries
library(ggplot2)
library(stats)

# Binomial distribution .......................................................
cat("Binomial distribution\n")

# Function computing binomial probability
binomial_probability <- function(x, n, p) {
  choose(n, x) * (p^x) * ((1 - p)^(n - x))
}

# Probability of 5 heads in 10 flips of a coin
x <- 5; n <- 10; p <- 1/2
probability1 <- binomial_probability(x, n, p)
probability2 <- dbinom(x, n, p)
cat(sprintf("\nProbability of getting %d heads in %d coin tosses: %.5f\n", x, n, probability1))
cat(sprintf("Probability of getting %d heads in %d coin tosses: %.5f\n", x, n, probability2))

# Probability of 3 times a 6 in 10 rolls of dice
x <- 3; n <- 10; p <- 1/6
probability1 <- binomial_probability(x, n, p)
probability2 <- dbinom(x, n, p)
cat(sprintf("\nProbability of getting %d 6s in %d dice rolls: %.5f\n", x, n, probability1))
cat(sprintf("Probability of getting %d 6s in %d dice rolls: %.5f\n", x, n, probability2))

# Probability of passing an (A, B, C) exam answering randomly
x <- 5; n <- 10; p <- 1/3
probability1 <- binomial_probability(x, n, p)
probability2 <- dbinom(x, n, p)
cat(sprintf("\nProbability of answering %d questions out of %d: %.5f\n", x, n, probability1))
cat(sprintf("Probability of answering %d questions out of %d: %.5f\n", x, n, probability2))

# Simulate 10 rolls of dice and plot probability distribution
x_vals <- 0:10
sixes <- dbinom(x_vals, 10, 1/6)
df <- data.frame(x = x_vals, pmf = sixes)

ggplot(df, aes(x = x, y = pmf)) +
  geom_bar(stat = "identity", fill = "red") +
  geom_point(color = "red", size = 3) +
  labs(x = "x", y = "B(x)", title = "Binomial Distribution") +
  theme_minimal()

# Compute mean and variance
mean <- 10 * (1/6)
var <- 10 * (1/6) * (5/6)
cat(sprintf("mean = %.2f\nvariance = %.2f\n", mean, var))


# Poisson distribution ........................................................
cat("Poisson distribution\n")

# Function computing poisson probability
poisson_probability <- function(x, lambda) {
  (lambda^x) * exp(-lambda) / factorial(x)
}

# Probability of 3 cancer patients with average 5
x <- 3; lambda <- 5
probability1 <- poisson_probability(x, lambda)
probability2 <- dpois(x, lambda)
cat(sprintf("\nProbability of observing %d cancer patients with lambda %.1f: %.5f\n", x, lambda, probability1))
cat(sprintf("Probability of observing %d cancer patients with lambda %.1f: %.5f\n", x, lambda, probability2))

# Probability of 5 or less patients, with same average
x <- 5
probability1 <- sum(dpois(0:x, lambda))
probability2 <- ppois(x, lambda)
cat(sprintf("\nProbability of observing %d or less cancer patients with lambda %.1f: %.5f\n", x, lambda, probability1))
cat(sprintf("Probability of observing %d or less cancer patients with lambda %.1f: %.5f\n", x, lambda, probability2))

# Probability of more than 5 patients, with same average
probability1 <- 1 - probability1
probability2 <- 1 - probability2
cat(sprintf("\nProbability of observing more than %d cancer patients with lambda %.1f: %.5f\n", x, lambda, probability1))
cat(sprintf("Probability of observing more than %d cancer patients with lambda %.1f: %.5f\n", x, lambda, probability2))

# Plot probability distribution
x_vals <- 0:15
impacts <- dpois(x_vals, 4)
df <- data.frame(x = x_vals, pmf = impacts)

ggplot(df, aes(x = x, y = pmf)) +
  geom_bar(stat = "identity", fill = "red") +
  geom_point(color = "red", size = 3) +
  labs(x = "x", y = "P(x)", title = "Poisson Distribution") +
  theme_minimal()

# Compute mean and variance
mean <- 4
var <- 4
cat(sprintf("mean = %.2f\nvariance = %.2f\n", mean, var))


# Gaussian distribution .......................................................
cat("Gaussian distribution\n")

# Function computing Gaussian density
gaussian_density <- function(x, mu, sigma) {
  pnorm(x, mean = mu, sd = sigma)
}

# Calculate probabilities
x1 <- 1; x2 <- 2; mu <- 1; sigma <- 2
probability1 <- gaussian_density(x2, mu, sigma) - gaussian_density(x1, mu, sigma)
probability2 <- pnorm(x2, mean = mu, sd = sigma) - pnorm(x1, mean = mu, sd = sigma)
cat(sprintf("\nProbability of the Gaussian distribution being between %.1f and %.1f: %.5f\n", x1, x2, probability1))
cat(sprintf("Probability of the Gaussian distribution being between %.1f and %.1f: %.5f\n", x1, x2, probability2))

# Plot Gaussian distribution
x <- seq(mu - 4 * sigma, mu + 4 * sigma, length.out = 1000)
gaussian_distribution <- dnorm(x, mean = mu, sd = sigma)
df <- data.frame(x = x, density = gaussian_distribution)

ggplot(df, aes(x = x, y = density)) +
  geom_line(color = "blue") +
  labs(x = "x", y = "Probability Density", title = "Gaussian Distribution") +
  theme_minimal()
