
# # list/set trick doesn't maintain order
# s1 = list(set([7,8,9,0,1,2,3,4,7,8,9,0]))
# s2 = list(set([7,8,9,0,2,3]))

s1 = [7,8,9,0,1,2,3,4,7,8,9,0]
s2 = [7,8,9,0,2,3]

def dedupe(lst):
    deduped_inorder = []
    for element in lst:
        if element not in deduped_inorder:
            deduped_inorder.append(element)
    return deduped_inorder

# print(dedupe(s1))
# print(dedupe(s2))


''' star arguments: *args'''
def star_args(*args):
    for item in args:
        print(item)
    return None

# star_args('hey', 5, int, [1,2,3,4,5])


''' Simple Union function for lists using "sets" '''
list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def union(set1, set2):
    set_union = []
    for item in set1:
        set_union.append(item)
    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

# print(union(list1, list2))

def union_mult_sets(*args):
    set_union = []

    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    return set_union

print(union_mult_sets(list1, list2, list3))



