# Import libraries
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Bernouilli distribution

# Bernoulli distribution with p = 1/6 .........................................
six = stats.bernoulli(1/6)

# Plot probability mass function
x = np.arange(2)
plt.plot(x,six.pmf(x), 'ro', ms=8)
plt.vlines(x, 0, six.pmf(x), colors='r', lw=4)
plt.show()

# Expected value
six.mean()

# Variance
six.var()

# Binomial distribution .......................................................

# Binomial distribution
sixes = stats.binom(10, 1/6)

# Plot probability mass function
x = np.arange(11)
plt.plot(x,sixes.pmf(x), 'ro', ms=8)
plt.vlines(x, 0, sixes.pmf(x), colors='r', lw=4)
plt.show()

# Plot cumulative distribution function
plt.step(x,sixes.cdf(x))
plt.show()

# Expected value
sixes.mean()

# Variance
sixes.var()

1 - sixes.pmf(0)

# Poisson distribution ........................................................

# Poisson distribution with average of 4 meteorite impacts per year
impacts = stats.poisson(4)

# Plot probability mass function
x = np.arange(16)
plt.plot(x,impacts.pmf(x), 'ro', ms=8)
plt.vlines(x, 0, impacts.pmf(x), colors='r', lw=4)
plt.show()

# Plot cumulative distribution function
plt.step(x,impacts.cdf(x))
plt.show()

# the expected value
impacts.mean()

# the variance
impacts.var()

impacts.cdf(4) - impacts.cdf(1)

# Uniform distribution ........................................................

# e.g. angle of a spinner
angle = stats.uniform(0,360)

# Plot probability density function
x = np.linspace(-30,390,100)
plt.plot(x, angle.pdf(x), color='r')
plt.show()

# Plot cumulative distribution function
plt.plot(x,angle.cdf(x))
plt.show()

# Mean
angle.mean()

# Variance
angle.var()

angle.cdf(180) - angle.cdf(90)

# Exponential distribution ....................................................

# e.g. an average of 4 meteorite impacts per year.
lam = 4
# X describes the time until the first meteorite impact, in years.
wait = stats.expon(0,1/lam)

# plot the probability density function
x = np.linspace(0,2,100)
plt.plot(x, wait.pdf(x), color='r')
plt.show()

# plot the cumulative distribution function
plt.plot(x,wait.cdf(x))
plt.show()

# the mean
wait.mean()

# the variance
wait.var()

wait.cdf(0.5)

# Gaussian distribution .......................................................

# Gaussian distribution
mu = 200
sigma = 20
thickness = stats.norm(mu,sigma)  # paper thickness in microns

# Plot probability density function
x = np.linspace(100,300,100)
plt.plot(x, thickness.pdf(x), color='r')
plt.show()

# Plot cumulative distribution function
plt.plot(x,thickness.cdf(x))
plt.show()

# Mean
thickness.mean()

# Variance
thickness.var()

1 - thickness.cdf(225)
