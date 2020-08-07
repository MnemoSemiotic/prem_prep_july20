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

print(dec_to_bin(43))