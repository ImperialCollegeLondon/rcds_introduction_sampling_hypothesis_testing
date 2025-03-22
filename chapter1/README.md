## RCDS - Introduction to probability & statistical inference

### Dr. Jesús Urtasun Elizari

### Imperial College London - 2024 / 2025

<img src="/readme_figures/grad-school-logo.png">

## Chapter 1. Introduction to probability & random events.

In this chapter we will describe random events and probability distributions.
We will focus on two main classes, the so-called *discrete* and *continous* events.
We will simulate some examples following the binomial, Poisson, and Gaussian distributions, 
and we will compare our manual calculations with the ones included in the `stats` package of the `scipy` library.

Create a Python script for this exercise by running the following command in your terminal.

```bash
touch random_variables.py
```

Open the file with `VScode`.

```bash
code random_variables.py
```

Import the libraries neeed for these examples.

```python

# Import libraries
import numpy as np
from math import comb, exp, factorial, erf, sqrt
from scipy import stats
import matplotlib.pyplot as plt

```

### Binomial distribution

Write the following function computing the binomial distribution for a given number of sucesses *x*, number of trials *n*, and individual probability *p*:

```python

# Function computing binomial probability
def binomial_probability(x, n, p):
    """
    Calculate the binomial probability of getting n successes in n trials
    with a probability of success p.
    """
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

```

Run the following code to check the numerical values. We will first compute it with the function we just defined, 
and then using the `binom` probability mass function, already included in the `stats` library.

```python

# Probability of 5 heads in 10 flips of a coin
x = 5; n = 10; p = 1/2
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability of getting {x} heads in {n} coin tosses: {probability1}")
print(f"Probability of getting {x} heads in {n} coin tosses: {probability2}")

# Probability of 3 times a 6 in 10 rolls of dice
x = 3; n = 10; p = 1/6
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability of getting {x} 6s in {n} dice rolls: {probability1}")
print(f"Probability of getting {x} 6s in {n} dice rolls: {probability2}")

# Probability of passing an (A, B, C) exam answering randomly
x = 5; n = 10; p = 1/3
probability1 = binomial_probability(x, n, p)
probability2 = stats.binom.pmf(x, n, p)
print(f"\nProbability of answering {x} 5 questions out of {n}: {probability1}")
print(f"Probability of answering {x} 5 questions out of {n}: {probability2}")

```

### Poisson distribution

Write the following function computing the Poisson distribution, for a given number of observations *x* and observed aberage *lmbda*.

```python

# Function computing poisson probability
def poisson_probability(x, lmbda):
    """
    Calculate the probability of observing x events in a Poisson distribution
    with rate parameter lmbda.
    """
    return (lmbda ** x) * exp(-lmbda) / factorial(x)

```

Run the following code to check the numerical values. We will first compute it with the function we just defined, 
and then using the `poisson` probability mass function, already included in the `stats` library.

```python

# Probability of 3 cancer patients with average 5
x = 3; lmbda = 5
probability1 = poisson_probability(x, lmbda)
probability2 = stats.poisson.pmf(x, lmbda)
print(f"\nProbability of observing {x} cancer patients with lambda {lmbda}: {probability1}")
print(f"Probability of observing {x} cancer patients with lambda {lmbda}: {probability2}")

# Probability of 5 or less patients, with same average
x = 5; lmbda = 5
probability1 = stats.poisson.pmf(0, lmbda) + stats.poisson.pmf(1, lmbda) + stats.poisson.pmf(2, lmbda) + stats.poisson.pmf(3, lmbda) + stats.poisson.pmf(4, lmbda) + stats.poisson.pmf(5, lmbda)
probability2 = stats.poisson.cdf(x, lmbda)
print(f"\nProbability of observing {x} or less cancer patients with lambda {lmbda}: {probability1}")
print(f"Probability of observing {x} or less cancer patients with lambda {lmbda}: {probability2}")

# Probability of more than 5 patients, with same average
x = 5; lmbda = 5
probability1 = 1 - probability1
probability2 = 1 - probability2
print(f"\nProbability of observing more than {x} patients with lambda {lmbda}: {probability1}")
print(f"Probability of observing moer than {x} patients with lambda {lmbda}: {probability2}")

```

### Gaussian distribution

Write the following function computing the Gaussian distribution, with a given mean value *mu* and standard deviation *sigma*:
The negative exponential squared, which gives the bell shape, is encoded in the *error function*, or `erf`, included in the `math` library.

```python

# Function computing gaussian probability
def gaussian_density(x, mu, sigma):
    """
    Calculate the probability of a Gaussian distribution at a given value x.
    """
    return erf((x - mu) / (sqrt(2) * sigma)) / 2

```

Run the following code to check the numerical values. We will first compute it with the function we just defined, 
and then using the *norm* probability mass function, already included in the `stats` library.
Remember that, for computing a probability in a continous case, we have to evaluate the probability distribution (or probability *density*),
in a specific range. This is why the `stats` library names them `cdf`, since it evaluates the difference of *cumulative* distributions.

```python

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

# Calculating probability of (-1sigma, 1sigma) 68% CI
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability = gaussian_density(sigma, mu, sigma) - gaussian_density(-sigma, mu, sigma)
print(f"\n68% ci: {probability}")

# Calculating probability of (-2sigma, 2sigma) 95% CI
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability = gaussian_density(2 * sigma, mu, sigma) - gaussian_density(-2 * sigma, mu, sigma)
print(f"\n95% ci: {probability}")

# Calculating probability of (-3sigma, 3sigma) 99% CI
x1 = -2; x2 = 2; mu = 1; sigma = 2
probability = gaussian_density(3 * sigma, mu, sigma) - gaussian_density(-3 * sigma, mu, sigma)
print(f"\n95% ci: {probability}")

```

Plot the Gaussian distribution:

```python

# Plot gaussian distrubtion
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
gaussian_distribution = stats.norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.plot(x, gaussian_distribution, label = f"mu = {mu}, sigma = {sigma}")
plt.xlabel('x'); plt.ylabel('Probability Density')
plt.legend(); plt.grid(True)
plt.title('Gaussian Distribution')
plt.show()

```
