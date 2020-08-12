from random import random

def bernoulli(p=0.5):
    if random() < p:
        return 1
    return 0


def perform_geometric(p=0.5):
    num_trials = 1

    for _ in range(20000):
        flip = bernoulli(p)
        num_trials += 1
        if flip == 1:
            break
        # print(f'trial: {flip}')
    print(f'Success! after {num_trials} trials!')

# perform_geometric(p=0.05)

