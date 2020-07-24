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

# urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
# farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# print('urban:', mean(urban))
# print('farmhouse:', mean(farmhouse))

# # print(sorted(urban))
# # print(sorted(urban)[1:-1])
# # print(sorted(farmhouse)[1:-1])
# print('urban:', mean(sorted(urban)[1:len(urban)-1]))
# print('farmhouse:', mean(sorted(farmhouse)[1:len(farmhouse)-1]))



'''Median'''

lst1 = 13, 18, 13, 14, 13, 16, 14, 21, 13
lst2 = 15, 14, 10, 8, 12, 8, 16, 13

# sort list
lst1_sorted = sorted(lst1)
lst2_sorted = sorted(lst2)

# print(lst1_sorted)
# print(lst2_sorted)

def median(lst):
    lst_sorted = sorted(lst)
    
    if len(lst) % 2 == 1:
        median_idx = int(len(lst) / 2)
        return lst_sorted[median_idx]
    else:
        higher_mid = lst_sorted[int(len(lst)/2)]
        lower_mid = lst_sorted[int(len(lst)/2)-1]

        return (higher_mid + lower_mid) / 2

print(median(lst1))
print(median(lst2))
    
