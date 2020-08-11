def factorial(n):
    if n < 0:
        return None

    prod = 1

    for i in range(2, n+1):
        prod *= i
    
    return prod

# print(factorial(5))

from math import e
def poisson_pmf(lmbda, k):
    return (lmbda**k * e**(-lmbda)) / factorial(k)

# print(poisson_pmf(10, 10))


'''
One average, 7 birds fly across your field of vision every 10 minutes when you're observing in a protected wetland. What is the probability of observing 12 birds in 20 minutes?
'''

lmbda = 14 # 7 birds in 10 minutes
k = 12
print(poisson_pmf(lmbda, k))