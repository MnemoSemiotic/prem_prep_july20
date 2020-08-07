def gen_4_bit_binary():
    bin_lst = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_lst[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_lst

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')


'''
decimal to binary algorithm
- take the modulus by 2
    - set aside the result
- floor divide by 2 until we get 0
- reverse the result
'''
# 43 % 2         ==> 1
# 43 // 2 = 21
# 21 % 2         ==> 1
# 21 // 2 = 10
# 10 % 2         ==> 0
# 10 // 2 = 5
# 5 % 2          ==> 1
# 5 // 2  = 2
# 2 % 2          ==> 0
# 2 // 2   = 1
# 1 % 2          ==> 1
# 1 // 2  = 0

def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1]

# print(dec_to_bin(43))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)
    return bins_d

# for dec, bin_ in get_binary().items():
#     print(f'{dec}: {bin_}')


def binomial_distr(binary_dict):
    binomial_dict = dict()

    for _, val in binary_dict.items():
        sum_ = sum(val)
        if sum_ not in binomial_dict:
            binomial_dict[sum_] = 0
        binomial_dict[sum_] += 1
    
    return binomial_dict

d = get_binary(n_bits=12)

binomial_dict = binomial_distr(d)

# for k, v in binomial_dict.items():
#     print(f'{k}: {v}')

for k, v in binomial_dict.items():
    print(f'{k}: {v / len(d.values())}')