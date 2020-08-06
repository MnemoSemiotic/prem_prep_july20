from random import choice

def coin_flip():
    flip_choices = ['H', 'T']
    return choice(flip_choices)


series_of_flips = []
for _ in range(20):
    series_of_flips.append(coin_flip())

# print(series_of_flips)


# 1st draw: P(Queen of Hearts) = 1/52
# 2nd draw: P(Queen | QoH on the first draw) = 3/51


# # heads on the first flip, tails on the 2nd flip, heads on the 3rd flip?
# 0.5*0.5*0.5 = 0.5**3 = 0.125

# # heads on the first flip, 3 on the roll of die, a tails, an odd number on the die roll?
# 0.5 * 1/6 * 0.5 * 0.5 = 0.208

'''Multiplication Rule!!'''


'''
factorial: 6! = ^*5*4*3*2*1, 0! = 1
* measure the cardinality of a sample space
'''
def factorial(num):
    prod = 1

    for i in range(1, num+1):
        prod *= i

    return prod

print(factorial(52))



