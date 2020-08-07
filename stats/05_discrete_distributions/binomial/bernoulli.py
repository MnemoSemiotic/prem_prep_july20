from random import choice, random

# rolling a die
die_possibilities = [1,2,3,4,5,6]

'''
X represents the outcome from rolling a 6-sided die
'''

X_1 = choice(die_possibilities)
X_2 = choice(die_possibilities)
X_3 = choice(die_possibilities)

# print(X_1)
# print(X_2)
# print(X_3)

'''
Y is a random variable that follows these rules
Y = 1 if the roll of a 6-sided die has an 
    even count of pips
Y = 0 if the roll has an odd count of pips
'''
def get_Y():
    if choice(die_possibilities) % 2 == 0:
        return 1
    else:
        return 0

Y_1 = get_Y()
Y_2 = get_Y()
Y_3 = get_Y()

# print(Y_1)
# print(Y_2)
# print(Y_3)





'''
Bernoulli - 1 of 2 outcomes, parameter: p, for probability
'''

def bernoulli(p_success=0.5):
    # draw = random()
    # print(draw)
    # if draw < p_success:
    #     return True
    # else:
    #     return False
    
    return random() < p_success
# print(bernoulli(p_success=0.25))


num_trials = 100000
trials_success = 0
p_success = 0.42
for _ in range(num_trials):
    if bernoulli(p_success):
        trials_success += 1
    
print(trials_success/num_trials)