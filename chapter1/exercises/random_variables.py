# RCDS Introduction to Statistics and random sampling
# Jesus Urtasun Elizari - Imperial College London
# Chapter 1 - Random variables and probability distributions


# Import libraries
import numpy as np
from math import comb, exp, factorial, erf, sqrt
from scipy import stats
import matplotlib.pyplot as plt


# Binomial distribution .......................................................
print("Binomial distribution")

# Function computing binomial probability
def binomial_probability(x, n, p):
    """
    Calculate the binomial probability of getting k successes in n trials
    with a probability of success p.
    """
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

# Calculating probability of 5 heads in 10 flips of a coin
x = 5; n = 10; p = 1/2
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability of getting {x} heads in {n} coin tosses: {probability1}")
print(f"Probability of getting {x} heads in {n} coin tosses: {probability2}")

# Calculating probability of 3 times a 6 in 10 rolls of dice
x = 3; n = 10; p = 1/6
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability of getting {x} 6s in {n} dice rolls: {probability1}")
print(f"Probability of getting {x} 6s in {n} dice rolls: {probability2}")

# Calculating probability of passing an (A, B, C) exam answering randomly
x = 5; n = 10; p = 1/3
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability of answering {x} 5 questions out of {n}: {probability1}")
print(f"Probability of answering {x} 5 questions out of {n}: {probability2}")

# Simulate 10 rolls of dice and plot probability distribution
x = np.arange(11)
sixes = stats.binom(10, 1/6)
plt.plot(x, sixes.pmf(x), "ro", ms = 8)
plt.vlines(x, 0, sixes.pmf(x), colors = "r", lw = 4)
plt.xlabel("x"); plt.ylabel("B(x)")
plt.title("Binomial distribution")
plt.show()

# Compute mean and variance
mean = sixes.mean()
var = sixes.var()
print("mean = ", round(mean, 2), "\nvariance = ", round(var, 2))


# Poisson distribution ........................................................
print("Poisson distribution")

# Function computing poisson probability
def poisson_probability(x, lmbda):
    """
    Calculate the probability of observing k events in a Poisson distribution
    with rate parameter lmbda.
    """
    return (lmbda ** x) * exp(-lmbda) / factorial(x)

# Calculating probability of 3 cancer patients with average 5
x = 3; lmbda = 5
probability1 = poisson_probability(x, lmbda)
probability2 = stats.poisson.pmf(x, lmbda)
print(f"\nProbability of observing {x} cancer patients with lambda {lmbda}: {probability1}")
print(f"Probability of observing {x} cancer patients with lambda {lmbda}: {probability2}")

# Calculating probability of 5 or less patients, with same average
x = 5; lmbda = 5
probability1 = stats.poisson.pmf(0, lmbda) + stats.poisson.pmf(1, lmbda) + stats.poisson.pmf(2, lmbda) + stats.poisson.pmf(3, lmbda) + stats.poisson.pmf(4, lmbda) + stats.poisson.pmf(5, lmbda)
probability2 = stats.poisson.cdf(x, lmbda)
print(f"\nProbability of observing {x} or less cancer patients with lambda {lmbda}: {probability1}")
print(f"Probability of observing {x} or less cancer patients with lambda {lmbda}: {probability2}")

# Calculating probability of more than 5 patients, with same average
x = 5; lmbda = 5
probability1 = 1 - probability1
probability2 = 1 - probability2
print(f"\nProbability of observing {x} or less cancer patients with lambda {lmbda}: {probability1}")
print(f"Probability of observing {x} or less cancer patients with lambda {lmbda}: {probability2}")

# Plot probability distribution
impacts = stats.poisson(4) # e.g. an average of 4 meteorite impacts per year.
x = np.arange(16)
plt.plot(x, impacts.pmf(x), "ro", ms = 8)
plt.vlines(x, 0, impacts.pmf(x), colors = "r", lw = 4)
plt.xlabel("x"); plt.ylabel("P(x)")
plt.title("Poisson distribution")
plt.show()

# Compute mean and variance
mean = impacts.mean()
var = impacts.var()
print("mean = ", round(mean, 2), "\nvariance = ", round(var, 2))


# Gaussian distribution .......................................................
print("Poisson distribution")

# Function computing gaussian probability
def gaussian_density(x, mu, sigma):
    """
    Calculate the probability of a Gaussian distribution falling between x1 and x2.
    """
    return erf((x - mu) / (sqrt(2) * sigma)) / 2

# Calculating probability
x1 = 1; x2 = 2; mu = 1; sigma = 2
probability1 = gaussian_density(x2, mu, sigma) - gaussian_density(x1, mu, sigma)
probability2 = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)
print(f"\nProbability of the Gaussian distribution being between {x1} and {x2}: {probability1}")
print(f"Probability of the Gaussian distribution being between {x1} and {x2}: {probability2}")

# Calculating probability
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability1 = gaussian_density(x2, mu, sigma) - gaussian_density(x1, mu, sigma)
probability2 = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)
print(f"\nProbability of the Gaussian distribution being between {x1} and {x2}: {probability1}")
print(f"Probability of the Gaussian distribution being between {x1} and {x2}: {probability2}")

# # Calculating probability of (-1sigma, 1sigma) 68% CI
# x1 = -2; x2 = 2; mu = 1; sigma = 2
# probability = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, -sigma)
# print(f"\n68% ci: {probability}")

# # Calculating probability of (-2sigma, 2sigma) 95% CI
# x1 = -2; x2 = 2; mu = 1; sigma = 2
# probability = stats.norm.cdf(x2, mu, 2*sigma) - stats.norm.cdf(x1, mu, -2*sigma)
# print(f"\n95% ci: {probability}")

# Plot gaussian distrubtion
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
gaussian_distribution = stats.norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.plot(x, gaussian_distribution, label = f"mu = {mu}, sigma = {sigma}")
plt.xlabel('x'); plt.ylabel('Probability Density')
plt.legend(); plt.grid(True)
plt.title('Gaussian Distribution')
plt.show()