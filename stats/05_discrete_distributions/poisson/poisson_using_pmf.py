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

def poisson_cdf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_cdf(lmbda, k)

    return d

d = poisson_cdf_dict(lmbda=10, low_k=0, high_k=20)

# for k, v in d.items():
#     print(f'{k}: {v}')


'''
You are observing a phenomenon that follows perfectly a poisson process. Given a certain number of observations (10,000), how many events would you expect for each value of k, given a lmbda of 10, low_k=0, to high_k=30?
'''
# print(round(poisson_pmf(10, 1) * 10000))

def poisson_counts(lmbda, low_k, high_k, num_samples=10000):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = round(poisson_pmf(lmbda, k) * num_samples)

    return d

d = poisson_counts(10, 0, 30, num_samples=100000)

# for k, v in d.items():
#     print(f'{k}: {v}')



'''
There's a busy intersection in Denver, on average where 30 cars pass by every 10 minutes. What is the probability that 40 cars will pass by if observing a new ten minute time period?
'''
# print(poisson_pmf(30, 40)) # 0.0139


'''
You have a data set from observing a stream where salmon swim by at a rate of 10 fish every 15 minutes. What is the probability that 15 fish swim by in 30 minutes?

lmbda = 20
'''
# print(poisson_pmf(20, 15)) # 0.0516


'''
In a volume of a certain compressed gas that is resampled daily, on average you would expect to observe 20 nitrogenous molecules. What is the probability that you would observe 25 or more of these molecules?

'''
# print(1 - poisson_cdf(20, 24)) # 0.157


'''
There's a dock with a 1000s and 1000s of barrels. On average there are 19 fish in a barrel. If you choose a barrel at random, what is the probability that that barrel has only 5 fish?
'''
# print(poisson_pmf(19, 5)) # 0.0001156
