'''
geometric pmf gives the probability of the number of trials up to and including the first success
k the trial where the first heads appears
k=6


or

gives the probability of the number of failures before the first success

k=5
'''



def geometric_pmf(p, k, inclusive=True):
    if inclusive: # k is the trial with the first success
        return p * (1-p)**(k-1)
    else: # k is the number of failures
        return p * (1-p)**k

'''
You are flipping a fair coin. What is the probability that you get your first heads on the 7th flip?
'''
# print(geometric_pmf(0.5, 7, inclusive=True))   # 0.0078125
# print(geometric_pmf(0.5, 6, inclusive=False))  # 0.0078125


'''
A roofer hits their thumb with a hammer 1/1000 times when they swing the hammer. What is the probability that the roofer will hit first hit their thumb after swinging the hammer 37 times (hits on the 38th)?
'''
# print(geometric_pmf((1/1000), 38, inclusive=True))  # 0.0009637
# print(geometric_pmf((1/1000), 37, inclusive=False)) # 0.0009637


'''
Geometric cdf
'''
def geom_cdf_closed(p, k, inclusive=True):
    if inclusive:
        return 1 - (1-p)**k
    else:
        return 1 - (1-p)**(k+1)


def geom_cdf_accum(p, k, inclusive=True):
    proba_ = 0

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0

    for r in range(starting_at, k+1):
        proba_ += geometric_pmf(p, r, inclusive=inclusive)

    return proba_

'''
You are flipping a fair coin. What is the probability that you will need to flip the coin less than 7 times before getting a heads?
'''

print(geom_cdf_closed(p=0.5, k=7, inclusive=True))  # 0.9921875
print(geom_cdf_closed(p=0.5, k=6, inclusive=False)) # 0.9921875
print(geom_cdf_accum(p=0.5, k=7, inclusive=True)) # 0.9921875
print(geom_cdf_accum(p=0.5, k=6, inclusive=False)) # 0.9921875
