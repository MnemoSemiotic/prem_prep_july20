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