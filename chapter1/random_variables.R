# LMS Introduction to statistics & hypothesis testing
# Jesús Urtasun Elizari - LMS Bioinformatics
# November 2023

# Chapter 1. Random variables & probability distributions

# Import libraries
library("statip")

# Set working directory
setwd("/Users/jurtasun/Desktop/Courses/LMS/2023/statistics_hypothesis_testing")

# i) Binomial distribution ....................................................

# Number of sixes rolling ten dice
n <- 10
p <- 1/6
x <- 0:n
pmf <- dbinom(x, n, p)

# Plot probability mass function
plot(x, pmf, main = "Binomial distribution", 
     ylim = c(0, 0.4), xlab = "x", ylab = "pmf(x)",
     type = "h", col = "red", axes = FALSE)
points(x, pmf, col = "red")
axis(side = 1, at = 0:10)
axis(side = 2)

# Probability of tossing 5 heads in 10 coins
dbinom(5, 10, 1/2)

# Probability of rolling 3 sixes in 10 dice
dbinom(3, 10, 1/6)

# Probability of answering correctly 5 out of 10 (a, b, c) questions of an exam
dbinom(5, 10, 1/3)

# ii) Poisson distribution ....................................................

# Poisson distribution with average 7
lambda = 7
x = 0:20
pmf <- dpois(x, lambda)

# Plot probability mass function
plot(x, pmf, main = "Poisson distribution",
     ylim = c(0, 0.25), xlab = "x", ylab = "pmf(x)",
     type = "h", col = "red", axes = FALSE)
points(x, pmf, col = "red")
axis(side = 1, at = x)
axis(side = 2)

# Probability of observing 3 cancer patients if average is 5
dpois(3, 5)

# Probability of observing 5 cancer patients in same hospital
dpois(5, 5)

# Probability of observing 5 or less cancer patients in same hospital - cumulative distribution
dpois(0, 5) + dpois(1, 5)  + dpois(2, 5) + dpois(3, 5) + dpois(4, 5)  + dpois(5, 5)
ppois(5, 5)

# Probability of observing more than 5 - unitarity
1 - ppois(5, 5)

# i) Gaussian distribution ....................................................

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

# Plot probability density function
x <- seq(-10, 10, 0.1)
pdf <- dnorm(x, mu, sigma)
plot(x, pdf, main = "Normal distribution", xlab = "x", type = "l", col = "red")

# Probability of measuring temperature between 2 and 3 degrees
pnorm(3, mu, sigma) - pnorm(2, mu, sigma)

# Probability of measuring between 0 and 3
pnorm(3, mu, sigma) - pnorm(0, mu, sigma)

# Probability of measuring between -5 and 5
pnorm(5, mu, sigma) - pnorm(-5, mu, sigma)

# ii) Confidence intervals ....................................................

# Probability of measuring between -std and std - 68% confidence interval
pnorm(sigma, mu, sigma) - pnorm(-sigma, mu, sigma)

# Probability of measuring between -2 std and 2 std - 95% confidence interval
pnorm(2 * sigma, mu, sigma) - pnorm(-2 * sigma, mu, sigma)

# Probability of measuring between -3 std and 3 std - 99% confidence interval
pnorm(3 * sigma, mu, sigma) - pnorm(-3 * sigma, mu, sigma)
