# RCDS Introduction to statistics & hypothesis testing
# Jesús Urtasun Elizari - ICL
# January 2024

# Chapter 1. Random variables & probability distributions

# Set working directory
setwd("/Users/jurtasun/Desktop/Courses/ICL/rcds_introduction_sampling_hypothesis_testing/chapter1/exercises")


# Binomial distribution .......................................................
print("Binomial distribution")

# rbinom()
# dbinom()
# pbinom()
# qbinom()

# Function computing binomial probability
binomial_probability <- function(n, k, p) {
  binom_coeff <- choose(n, k)
  prob <- binom_coeff * (p ^ k) * ((1 - p) ^ (n - k))
  return(prob)
}

# Calculating probability of 5 heads in 10 flips of a coin
probability1 <- binomial_probability(5, 10, 1/2)
probability2 <- dbinom(5, 10, 1/2)
print("probability1: ", probability1, "\nprobability2: ", probability2)

# Calculating probability of 3 times a 6 in 10 rolls of dice
probability1 <- binom_prob_explicit(3, 10, 1/6)
probability2 <- dbinom(3, 10, 1/6)
print("probability1: ", probability1, "\nprobability2: ", probability2)

# Calculating probability of passing an (A, B, C) exam answering randomly
probability1 <- binom_prob_explicit(5, 10, 1/3)
probability2 <- dbinom(5, 10, 1/3)
print("probability1: ", probability1, "\nprobability2: ", probability2)


# Poisson distribution ........................................................
print("Poisson distribution")

# rpois()
# dpois()
# ppois()
# qpois()

# Function computing Poisson distribution
poisson_probability <- function(lam, k) {
  prob <- (lam ^ k) * exp(-lam) / factorial(k)
  return(prob)
}

# Probability of observing 3 cancer patients if average is 5
probability1 <- poisson_probability(3, 5)
probability2 <- dpois(3, 5)
print("probability1: ", probability1, "\nprobability2: ", probability2)

# Probability of observing 5 cancer patients in same hospital
probability1 <- poisson_probability(5, 5)
probability2 <- dpois(5, 5)

# Probability of observing 5 or less cancer patients in same hospital

# Cumulative distribution - sum of individual probabilities
dpois(0, 5) + dpois(1, 5)  + dpois(2, 5) + dpois(3, 5) + dpois(4, 5)  + dpois(5, 5)

# Cumulative distribution
ppois(5, 5)

# Probability of observing more than 5 - unitarity
1 - ppois(5, 5)


# Gaussian distribution ....................................................
print("Gaussian distribution")

# rnorm()
# dnorm()
# pnorm()
# qnorm()

# Gaussian PDF using explicit formula
gaussian_probability <- function(x, mu, sigma) {
  coeff <- 1 / (sqrt(2 * pi) * sigma)
  exponent <- exp(-((x - mu) ^ 2) / (2 * sigma ^ 2))
  return(coeff * exponent)
}

# Set mean and standard deviation
mu <- 2
sigma <- 3

# Plot probability density function
x <- seq(-10, 10, 0.1)
pdf <- dnorm(x, mu, sigma)
plot(x, pdf, main = "Gaussian distribution", xlab = "x", type = "l", col = "red")

# Set mean and standard deviation
mu <- 0
sigma <- 1

# Probability of measuring temperature between 2 and 3 degrees
pnorm(3, mu, sigma) - pnorm(2, mu, sigma)

# Probability of measuring between 0 and 3
pnorm(3, mu, sigma) - pnorm(0, mu, sigma)

# Probability of measuring between -5 and 5
pnorm(5, mu, sigma) - pnorm(-5, mu, sigma)


# Confidence intervals ........................................................

# Probability of measuring between -std and std - 68% confidence interval
pnorm(sigma, mu, sigma) - pnorm(-sigma, mu, sigma)

# Probability of measuring between -2 std and 2 std - 95% confidence interval
pnorm(2 * sigma, mu, sigma) - pnorm(-2 * sigma, mu, sigma)

# Probability of measuring between -3 std and 3 std - 99% confidence interval
pnorm(3 * sigma, mu, sigma) - pnorm(-3 * sigma, mu, sigma)
