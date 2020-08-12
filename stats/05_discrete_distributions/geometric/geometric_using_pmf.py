'''
geometric pmf gives the probability of the number of trials up to and including the first success
k the trial where the first heads appears
k=6


or

gives the probability of the number of failures before the first success

k=5
'''



def geometric_pmf(p, k, inclusive=True):
    if inclusive:
        return p * (1-p)**(k-1)
    else:
        return p * (1-p)**k


'''
You are flipping a fair coin. What is the probability that you get a heads on the 7th flip?
'''


