def mean(lst):
    return sum(lst) / len(lst)

# # using the accumulator pattern
# def mean(lst):
#     accum = 0
#     for num in lst:
#         accum += num

#     return accum / len(lst)

# lst1 = [1,2,3,4,5,6,7,8,9]
# print(mean(lst1))

urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

print('urban:', mean(urban))
print('farmhouse:', mean(farmhouse))

# print(sorted(urban))
# print(sorted(urban)[1:-1])
# print(sorted(farmhouse)[1:-1])
print('urban:', mean(sorted(urban)[1:len(urban)-1]))
print('farmhouse:', mean(sorted(farmhouse)[1:len(farmhouse)-1]))