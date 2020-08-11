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

def binary_sampling_dict(n_bits, num_samples=500):
    d = {}

    for _ in range(num_samples):
        binary = generate_n_bits(n=n_bits)
        sum_bits = sum(binary)

        if sum_bits not in d:
            d[sum_bits] = 0
        d[sum_bits] += 1
    return d


''' one trial of 1000 samples '''
d = binary_sampling_dict(n_bits=8, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


''' 500 trials of 1000 samples '''
def binary_sampling_clt(n_bits, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = int(sum(v) / len(v))

    return d_out
    

for k, v in sorted(binary_sampling_clt(n_bits=8, num_samples=500, num_sample_trials=1000).items()):
    print(f'{k}: {v}')
