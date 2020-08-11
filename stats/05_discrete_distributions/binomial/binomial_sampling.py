from random import choice

def get_bit():
    return choice([0,1])

# print(get_bit())

def generate_n_bits(n=8):
    lst = []
    for _ in range(n):
        lst.append(get_bit())

    return lst

# print(generate_n_bits())