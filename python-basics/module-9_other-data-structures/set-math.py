numbers_1 = {7, 77, 777, 7777}
numbers_2 = {7, 88, 777, 8888}
numbers_3 = {7, 777}
numbers_4 = {8, 99, 888, 9999}

print(numbers_1, numbers_2)
print()

print('union:', numbers_1.union(numbers_2))
print('union:', numbers_1 | numbers_2)
print()

print('intersection:', numbers_1.intersection(numbers_2))
print('intersection:', numbers_1 & numbers_2)
print()

print('difference s1 - s2:', numbers_1.difference(numbers_2))
print('difference s1 - s2:', numbers_1 - numbers_2)
print('difference s2 - s1:', numbers_2.difference(numbers_1))
print('difference s2 - s1:', numbers_2 - numbers_1)
print()

print('symmetric difference:', numbers_1.symmetric_difference(numbers_2))
print('symmetric difference:', numbers_1 ^ numbers_2)
print()

print('s2 is subset of s1?', numbers_2.issubset(numbers_1))
print('s3 is subset of s1?', numbers_3.issubset(numbers_1))
print()

print('s1 is superset of s2?', numbers_1.issuperset(numbers_2))
print('s1 is superset of s3?', numbers_1.issuperset(numbers_3))
print()

print('s2 is disjoint from s1?', numbers_2.isdisjoint(numbers_1))
print('s4 is disjoint from s1?', numbers_4.isdisjoint(numbers_1))
