from sets import union, union_mult_sets, intersection, intersection_mult, complement, difference


setA = set(['bear', 'cat', 'dog', 'dolphin', 'weasel'])
setB = set(['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion'])
setC = set(['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog'])

sample_space = setA.union(setB).union(setC)
# print(sample_space)
print(len(setA) / len(sample_space))


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
a = True
b = False
c = True
# print(setA.union(setB.intersection(setC)) == (setA.union(setB)).intersection(setA.union(setC)))

# print((a or (b and c)) == (a and b) or (a and c))


'''
Idempotent Laws
A ∪ A = A
AA = A
'''
a = True
b = False
c = True
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
a = True
b = False
c = True
# print(setA.intersection(sample_space) == setA)

U = {True, False}
A = {True}
null_set = set()

# print(A.intersection(U) == A)
# print(A.intersection(null_set) == null_set)


'''
Absorption Laws
A ∪ (AB) = A
A(A ∪ B) = A
'''
# print(setA.union(setA.intersection(setB)) == setA)
# print(setA.intersection(setA.union(setB)) == setA)

# print(a or (a and b) == a)
# print(a and (a or b) == a)


'''
Identity Property
A ∪ ∅ = A
'''
# print(setA.union(null_set) == setA)

'''
Other axioms of set theory
Involution Law
(A^c)^c = A

we don't know the name of this
AB ∪ AB^c = A
'''
# print(not (not a) == a)
# print(((a and b) or (a and not b)) == a)


'''
DeMorgan’s Laws
1st: (A ∪ B)^c = A^cB^c

2nd: (AB)^c = A^c ∪ B^c
'''
# print((not (a or b)) == (not a) and (not b))
# print(not (a and b) == (not a) or (not b))
