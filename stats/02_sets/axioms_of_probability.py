from sets import union, union_mult_sets, intersection, intersection_mult, complement, difference


setA = set(['bear', 'cat', 'dog', 'dolphin', 'weasel'])
setB = set(['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion'])
setC = set(['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog'])

sample_space = setA.union(setB).union(setC)
# print(sample_space)



'''
Commutative
A ∪ B = B ∪ A
AB = BA
'''
# print(setA.union(setB) == setB.union(setA))
# print(setA.intersection(setB) == setB.intersection(setA))
a = True
b = False
c = True
# print((a or b) == (b or a))
# print((a and b) == (b and a))


'''
Associative
(A ∪ B) ∪ C = A ∪ (B ∪ C) = A ∪ B ∪ C 
(AB)C = A(BC) = ABC
'''
a = True
b = False
c = True

# print(((a or b) or c) == (a or (b or c)))


'''
A ∪ (BC) = (A ∪ B)(A ∪ C) 
A(B ∪ C) = (AB) ∪ (AC)
'''
# print(setA.union(setB.intersection(setC)) == (setA.union(setB)).intersection(setA.union(setC)))

# print((a or (b and c)) == (a and b) or (a and c))


'''
Idempotent Laws
A ∪ A = A
AA = A
'''
# print(setA.union(setA) == setA)
# print((a and a) == a)


'''
Domination Laws
Aside: 
U = Universal Set
The set of which all other subsets are a subset of
∅  = Empty Set = { }
A ∩ U = A
A ∩ ∅ = ∅
'''
# print(setA.intersection(sample_space) == setA)

U = {True, False}
A = {True}
null_set = set()

print(A.intersection(U) == A)
print(A.intersection(null_set) == null_set)