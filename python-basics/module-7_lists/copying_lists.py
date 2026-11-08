import copy

original_list = ['s', 'e', 'v', 'e', 'n']
referenced_original = original_list
copy_of_original = original_list.copy()
print(original_list, referenced_original)
referenced_original.pop(2)
print(original_list, referenced_original, copy_of_original)
print()

original_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
shallow_copy_of_original = original_matrix.copy()
deep_copy_of_original = copy.deepcopy(original_matrix)
print(original_matrix)
print(shallow_copy_of_original)

shallow_copy_of_original[-1].pop()
print(original_matrix)
print(shallow_copy_of_original)
print(deep_copy_of_original)

