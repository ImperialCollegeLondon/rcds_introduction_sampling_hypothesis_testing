# LMS Introduction to statistics & hypothesis testing
# Jesús Urtasun Elizari - LMS Bioinformatics
# November 2023

# Chapter 3. Introduction to hypothesis testing

# Import libraries
library("ggplot2")

# Set working directory
setwd("/Users/jurtasun/Desktop/Courses/LMS/2023/statistics_hypothesis_testing")

# i) Example 1: rolling dice ..................................................

# You have agreed to roll a die to decide who starts a game
# You are not sure if your opponent is using a loaded die
# You observe the following outcomes from 100 rolls of his die:
data <- c(6, 1, 5, 6, 2, 6, 4, 3, 4, 6, 1, 2, 5, 6, 6, 3, 6, 2, 6, 4, 6, 2,
          5, 4, 2, 3, 3, 6, 6, 1, 2, 5, 6, 4, 6, 2, 1, 3, 6, 5, 4, 5, 6, 3,
          6, 6, 1, 4, 6, 6, 6, 6, 6, 2, 3, 1, 6, 4, 3, 6, 2, 4, 6, 6, 6, 5,
          6, 2, 1, 6, 6, 4, 3, 6, 5, 6, 6, 2, 6, 3, 6, 6, 1, 4, 6, 4, 2, 6,
          6, 5, 2, 6, 6, 4, 3, 1, 6, 6, 5, 5)

# Do you have enough evidence to confront and ask for another die?
hist(data, main = "Observed data")

# Write down null and alternative hypotheses
# H0: p = 1/6
# H1: p > 1/6

# Choose a significance level
alpha = 0.01

# Code the data such that 6 = success and {0 - 5} = failure
six <- data == 6
print(six)

# Find length of data and number of sixes observed
n <- length(data)
x <- sum(six)
cat(x, "6s observed in", n, "rolls of a die")

# Use H0 (p = 1/6) to find the p-value for this particular observation
pval <- 1 - pbinom(x, 100, 1/6)
cat("p-value = ", pval, "\nsignificance level = ", alpha)

# p-value is less than alpha, so we reject H0: There is evidence that the die is loaded at the 1% significance level

# ii) Example 2 - tossing coins ...............................................

# Same person challenges you now to flip a coin to decide who starts the game
# You start to suspect the coin your opponent is using is not a fair one
# He/she flips it 50 times for you, with the following results: (1 = heads, 0 = tails):
data <- c(1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 
          1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1)

# Does the coin appear to be fair? If not, should you pick heads or tails?
hist(data, main = "Observed data")

# Write down null and alternative hypotheses
# H0: p = 1/2
# H1: p != 1/2 - we will use a 2-tailed test

# Choose a significance level
alpha = 0.05

# Find length of data and number of heads observed
n <- length(data)
h <- sum(data)
cat(h, "6s observed in", n, "rolls of a die")

# Use H0 to find the p-value of the observed number of heads
x1 <- 20 # the lower tail

# Compute p-value
p1 <- pbinom(x1, 50, 0.5)
pval <- 2 * p1 # double the p-value for a two-tailed test
cat("p-value = ", pval, "\nsignificance level = ", alpha)

# p-value is greater than alpha, so we accept H0: there is no evidence that the coin is biased at the 5% significance level

# iii) Example 3 - t test......................................................

# We use the t test to assess whether two samples taken from normal distributions have significantly different means.
# The test statistic follows a Student's t-distribution, provided that the variances of the two groups are equal.
# Other variants of the t-test are applicable under different conditions.
# The test statistic (...)

# The birth weights of babies (in kg) have been measured for a sample of mothers split into two categories: nonsmoking and heavy smoking.
# The two categories are measured independently from each other.
# Both come from normal distributions
# The two groups are assumed to have the same unknown variance:
data_nonsmoking <- c(3.99, 3.79, 3.60, 3.73, 3.21, 3.60, 4.08, 3.61, 3.83, 3.31, 4.13, 3.26, 3.54)
data_heavysmoking <- c(3.18, 2.84, 2.90, 3.27, 3.85, 3.52, 3.23, 2.76, 3.60, 3.75, 3.59, 3.63, 2.38, 2.34, 2.44)

# We want to know whether there is a significant difference in mean birth weight between the two categories.
plot(data_nonsmoking, main = "Data non smoking")
plot(data_heavysmoking, main = "Data heavy smoking")

# Write down null and alternative hypotheses:
# H0: there is no difference in mean birth weight between groups: d == 0
# H1: there is a difference, d != 0

# Choose a significance level
alpha = 0.05

# Get sample sizes
n_ns <- length(data_nonsmoking)
n_hs <- length(data_heavysmoking)

# Find mean and std
mean_ns <- mean(data_nonsmoking)
mean_hs <- mean(data_heavysmoking)
s_ns <- sd(data_nonsmoking)
s_hs <- sd(data_heavysmoking)
cat("non-smoking: n = ", n_ns, ", mean = ", mean_ns, ", SD = ", s_ns)
cat("heavy smoking: n = ", n_hs, ", mean = ", mean_hs, ", SD = ", s_hs)

# Difference between the two sample means:
d_obs <- mean_ns - mean_hs

# Pooled standard deviation
sp <- sqrt(((n_ns - 1)*s_ns^2 + (n_hs - 1)*s_hs^2)/(n_ns + n_hs - 2))

# t-test statistic
t_obs <- d_obs/(sp * sqrt(1/n_ns + 1/n_hs))

# Degrees of freedom given by n1 + n2 - 2
df <- n_ns + n_hs - 2

# Critical value for 95% of probability mass
t_95 <- qt(1 - 0.05/2, df)
cat("t observed = ", t_obs, "\nconfidence interval = (", t_95, ", ", -t_95, ")")

# t_obs lies outside the 95% confidence interval [-t95, t95], so we reject H0
