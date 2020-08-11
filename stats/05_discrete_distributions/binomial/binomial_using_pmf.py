
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))

# print(binomial_pmf(8, 4, p=0.25))


def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0

    for k in range(k_high+1):
        cumulative += binomial_pmf(n, k, p)
    
    return cumulative

# print(binomial_cdf(n=8, k=4, p=0.25))

def binomial_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, k, p=p) 

    return d

# for k, v in binomial_dict(8, 0,  8, 0.25).items():
#     print(f'{k}: {v}')


'''There are 8 components in parallel and at least 3 of those components need to be operational for a circuit to function. The probability of any given component being operational is 0.7. What is the probability that 3 components are operational?'''


# print(binomial_pmf(8, 3, p=0.7))


'''What is the probability that at least 3 components are operational?'''

# P(X = 3) + P(X = 4) ... P(X = 8)
# print(binomial_pmf(8, 3, p=0.7)+binomial_pmf(8, 4, p=0.7)+binomial_pmf(8, 5, p=0.7)+binomial_pmf(8, 6, p=0.7)+binomial_pmf(8, 7, p=0.7)+binomial_pmf(8, 8, p=0.7))

# print(1 - (binomial_pmf(8, 2, p=0.7)+binomial_pmf(8, 1, p=0.7+binomial_pmf(8, 0, p=0.7))))

# print(1 - binomial_cdf(8, 2, p=0.7))

# for k, v in binomial_dict(8, 0, 8, p=0.7).items():
#     print(f'{k}: {v}')



'''
Suppose you independently flip a coin 5 times and the outcome of each toss is equally probable for a heads or a tails. What is the probability of obtaining exactly 2 tails?
'''
# print(binomial_pmf(5, 2))


'''
Suppose you are building some sort of machine that relies on a specific component. The component is very delicate and the probability of it failing is 0.32. You decide to install 3 of these components in parallel, such that they are independent to each other, to ensure that you only need 1 to work to get your machine working. 

'''
# # What is the probability that exactly 1 of these components work?
# p = 1 - 0.32
# k = 1
# n = 3

# print(binomial_pmf(n, k, p))

# # What is the probability that 1 or more of these components work?
# print(binomial_pmf(n, 1, p) + binomial_pmf(n, 2, p) + binomial_pmf(n, 3, p))
# print(1 - binomial_pmf(n, 0, p))
