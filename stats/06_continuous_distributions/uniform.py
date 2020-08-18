from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    return_list = []

    for _ in range(n):
        return_list.append(get_bit())
    return return_list

# print(get_binary(n=32))

def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0.0
    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**(idx)
    
    return float_accum

# print(get_float(n=32))

'''
Using this scheme, what is the probability of getting a random float less than 0.752?
'''

d = dict()

d['> 0.752'] = 0
d['<= 0.752'] = 0

for _ in range(100000):
    flt = get_float(n=32)
    if flt > 0.752:
        d['> 0.752'] += 1
    else:
        d['<= 0.752'] += 1


d['> 0.752'] /= 100000
d['<= 0.752'] /= 100000
print(d)