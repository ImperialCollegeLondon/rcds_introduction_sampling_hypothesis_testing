# Install packages
# install.packages("statip")
library(statip)

set_plot_dimensions <- function(width_choice, height_choice) {
      options(repr.plot.width=width_choice, repr.plot.height=height_choice)
}

# Bernoulli distribution .....................................................

# Bernoulli distribution with p=1/6
p <- 1/6
x <- 0:1
pmf <- dbern(x,p)

# Plot probability mass function
set_plot_dimensions(4, 4)
plot(x, pmf, ylim=c(0,1), xlab="x", type="h", col="red", axes=FALSE)
points(x, pmf, col="red")
axis(side=1, at=c(0,1))
axis(side=2)

# Expected value = p
expectation <- sum(x * pmf)
expectation

# Variance = p * (1-p)
variance <- sum( (x - expectation)^2 * pmf)
variance

# Binomial distribution .......................................................

# Binomial distribution with n=10, p=1/6
n <- 10
p <- 1/6
x <- 0:n
pmf <- dbinom(x,n,p)

# Plot probability mass function
set_plot_dimensions(5, 4)
plot(x, pmf, ylim=c(0,0.4), xlab="x", type="h", col="red", axes=FALSE)
points(x, pmf, col="red")
axis(side=1, at=0:10)
axis(side=2)

# Plot cumulative distribution function
cdf <- pbinom(x,n,p)
set_plot_dimensions(5, 4)
plot(x, cdf, ylim=c(0,1), xlab="x", type="s", col="blue", axes=FALSE)
axis(side=1, at=x)
axis(side=2)

# the expected value = n * p
Expectation <- sum(x * pmf)
Expectation

# Variance = n * p * (1-p)
variance <- sum( (x - expectation)^2 * pmf)
variance

# Poisson distribution ........................................................

lambda = 4 # e.g. an average of 4 meteorite impacts per year

# Plot probability mass function
x = 0:16
pmf <- dpois(x,lambda)  # a Poisson distribution with lambda=4

set_plot_dimensions(5, 4)
plot(x, pmf, ylim=c(0,0.25), xlab="x", type="h", col="red", axes=FALSE)
points(x, pmf, col="red")
axis(side=1, at=x)
axis(side=2)

# Plot cumulative distribution function
cdf <- ppois(x,lambda)
set_plot_dimensions(5, 4)
plot(x, cdf, ylim=c(0,1), xlab="x", type="s", col="blue", axes=FALSE)
axis(side=1, at=x)
axis(side=2)

# the expected value = lambda
expectation <- sum(x * pmf)  # approximates the sum for x->infinity
expectation

# the variance = lambda
variance <- sum( (x - expectation)^2 * pmf) # approximates the sum for x->infinity
variance

ppois(4,lambda) - ppois(1,lambda) # using the CDF

# Uniform distribution ........................................................

# e.g. angle of a spinner.
a <- 0
b <- 360

# Plot probability density function
wid <- 0.001
x <- seq(-90,450,wid)
pdf <- dunif(x,a,b)  # a uniform distribution between 0 and 360
set_plot_dimensions(5, 4)
plot(x, pdf, xlab="x", ylim=c(0,0.004), type="l", col="red")

# Plot cumulative distribution function
cdf <- punif(x,a,b)  # a uniform distribution between 0 and 360
set_plot_dimensions(5, 4)
plot(x, cdf, xlab="x", ylim=c(0,1), type="l", col="blue")

# the expected value = 0.5 * (a + b)
expectation <- sum(x * pdf * wid)  # approximates the integral of (x * pdf(x))
expectation

# the variance = 1/12 * (b - a)^2
# approximating the integral of [(x - expectation)^2 * pdf] dx
variance <- sum( (x - expectation)^2 * pdf * wid)
variance

punif(180,a,b) - punif(90,a,b)  # using the CDF

# Gaussian distribution .......................................................

# X represents paper thickness in microns
mu <- 200
sigma <- 20

# Plot probability density function
wid <- 0.001
x <- seq(100,300,wid)
pdf <- dnorm(x,mu,sigma)  # a normal distribution
set_plot_dimensions(5, 4)
plot(x, pdf, xlab="x", type="l", col="red")

# Plot cumulative distribution function
cdf <- pnorm(x,mu,sigma)
set_plot_dimensions(5, 4)
plot(x, cdf, xlab="x", ylim=c(0,1), type="l", col="blue")

# the expected value = mu
expectation <- sum(x * pdf * wid)  # approximates the integral of [x * pdf(x)] dx
expectation

# the variance = (sigma)^2
# approximating the integral of [(x - expectation)^2 * pdf] dx
variance <- sum( (x - expectation)^2 * pdf * wid)  
variance

1 - pnorm(225,mu,sigma) # using the CDF

# Exponential distribution ....................................................

# X describes the time until the first meteorite impact, in years.
lambda <- 4  # e.g. an average of 4 meteorite impacts per year.

# plot the probability density function
wid <- 0.001
x <- seq(0,10,wid)
pdf <- dexp(x,lambda)  # an exponential distribution with rate = 4
set_plot_dimensions(5, 4)
plot(x, pdf, xlab="x", xlim=c(0,1.5), type="l", col="red")

# plot the cumulative distribution function
cdf <- pexp(x,lambda)
set_plot_dimensions(5, 4)
plot(x, cdf, xlab="x", xlim=c(0,1.5), ylim=c(0,1), type="l", col="blue")

# the expected value = 1/lambda
expectation <- sum(x * pdf * wid)  # approximates the integral of [x * pdf(x)] dx
expectation

# the variance = (1/lambda)^2
# approximating the integral of [(x - expectation)^2 * pdf] dx
variance <- sum( (x - expectation)^2 * pdf * wid)  
variance

pexp(0.5,lambda)
