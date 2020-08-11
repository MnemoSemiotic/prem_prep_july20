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
On average, 7 birds fly across your field of vision every 10 minutes when you're observing in a protected wetland. What is the probability of observing 12 birds in 20 minutes?
'''

lmbda = 14 # 7 birds in 10 minutes
k = 12
# print(poisson_pmf(lmbda, k))


'''
(essentially the same problem, but using the cdf)
On average, 7 components fail in a factory every 10 minutes during the workday. What is the probability of 12 or less components failing in 20 minutes?
'''
def poisson_cdf(lmbda, k_high):
    cdf = 0

    for k in range(k_high+1):
        cdf += poisson_pmf(lmbda, k)

    return cdf

# print(poisson_cdf(lmbda=14, k_high=12))

def poisson_pmf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lmbda, k)

    return d

d = poisson_pmf_dict(lmbda=10, low_k=0, high_k=20)

# for k, v in d.items():
#     print(f'{k}: {v}')


# for k, v in d.items():
#     print(f'{k}: {"*" * int(v * 100)}')