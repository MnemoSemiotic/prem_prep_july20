base_5 = [0,1,2,3,4,]
basic_counting = []
for num in base_5:
    for num2 in base_5:
        for num3 in base_5:
            for num4 in base_5:
                for num5 in base_5:
                    basic_counting.append([num,num2,num3,num4,num5,])

# for number in basic_counting:
#     print(number)

sample_space = []

for lst in basic_counting:
    valid_for_sample_space = True
    for number in lst:
        if lst.count(number) > 1:
            valid_for_sample_space = False
            break
    
    if valid_for_sample_space:
        sample_space.append(lst)

# for samp in sample_space:
#     print(samp)
# print('base 5: ',len(basic_counting))
# print('5 factorial: ',len(sample_space))


''' factorial '''
def factorial(num):
    prod = 1

    for i in range(1, num+1):
        prod *= i

    return prod

# print(factorial(52))



'''
Given a race in which there are 30 numbered runners to choose from, and 5 runners will get the top 5 positions, how many possible outcomes are there, assuming that the order in which the runners finish does matter?
'''

def perm(n, k):
    return int(factorial(n) / factorial(n-k))

# print(perm(30, 5))



def permutations_nP3(base=5):
    base_list = []

    for i in range(base):
        for j in range(base):
            for k in range(base):
                base_list.append([i, j, k])

    permutations = []

    for arrangement in base_list:
        if len(list(set(arrangement))) == 3:
            permutations.append(arrangement)

    return permutations

perms = permutations_nP3(base=5)
# for p in perms:
#     print(p)
# print(len(perms))
# print(perm(n=5, k=3))


''' 20C3 Out of a set of 20 basketball players you can only have 5 on the court at a time. How many combinations are there of your basketball team? '''

''' combinations '''
def comb(n, k): 
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

# print(comb(21, 5))


def combinations_intuition():
    twentyone_nums = list(range(1, 21+1))

    # find every arrangement of 5
    possible_3 = []

    for i in twentyone_nums:
        for j in twentyone_nums:
            for k in twentyone_nums:
                possible_3.append([i,j,k])

    permutations = []

    for three in possible_3:
        if len(list(set(three))) == 3:
            permutations.append(three)

    combinations = []

    for three in permutations:
        sorted_three= sorted(three)
        if sorted_three not in combinations:
            combinations.append(sorted_three)
        
    return combinations

# break_at = 30
# for comb in combinations_intuition():
#     print(comb)
#     break_at -= 1
#     if break_at < 0:
#         break


'''
Sampling approach to perms and combs
'''
from random import choice


'''
permutations
'''

def get_permutation(vals=[0,1,2,3,4], length=5):
    output = []

    for i in range(1000):
        if len(output) == length:
            # print(f'    took {i} iterations')
            break

        val = choice(vals)

        if val not in output:
            output.append(val)

    return output

# print(get_permutation(vals=['dog', 'cat', 'bunny'], length=2))

def build_permutations(vals=[0,1,2,3,4], exp_len=5):
    draws = 0

    permutations = []

    while len(permutations) < int(perm(len(vals), exp_len)):
        arrang = get_permutation(vals, exp_len)
        draws += 1

        if arrang not in permutations:
            permutations.append(arrang)

    return sorted(permutations), draws


perms = build_permutations(['elephant', 'hippo', 'jellyfish', 'squid', 'pill bug'], exp_len=3)

# for perm in perms[0]:
#     print(perm)

print(f'number of permutations: {len(perms[0])}')
print(f'took {perms[1]} draws')



'''
combinations
'''

def get_combination(vals=list(range(1,21)), length=3):
    output = []

    for _ in range(1000):
        if len(output) == length:
            break

        num = choice(vals)

        if num not in output:
            output.append(num)

    return sorted(output)

def build_combinations(vals=list(range(1,21)), length=3):
    draws = 0

    combinations = []

    while len(combinations) < int(comb(len(vals), length)):
        arrang = get_combination(vals, length)
        draws += 1

        if arrang not in combinations:
            combinations.append(arrang)

    return combinations, draws

combs, draws = build_combinations(['elephant', 'hippo', 'jellyfish', 'squid', 'pill bug'], length=3)

# for comb in combs:
#     print(comb)

print(f'number of combinations: {len(combs)}')
print(f'took {draws} draws')