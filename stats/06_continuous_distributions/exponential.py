from math import e

def exponential_pdf(lmbda, x):
    if x < 0: return 0
    return lmbda * e**(-lmbda * x)

def exponential_cdf(lmbda, x):
    if x < 0: return 0
    return 1 - e**(-lmbda * x)

def exponential_mean(lmbda):
    return 1 / lmbda

def exponential_variance(lmbda):
    return 1 / lmbda**2