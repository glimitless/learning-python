empty = []
letters = ["a", "b", "c"]
letters2 = list("blue")
numbers = [1, 2, 3]
numbers2 = list(range(1,4))
mixed = [None, True, 3, "Four"]
print(empty, type(empty))
print(letters, type(letters))
print(letters2, type(letters2))
print(numbers, type(numbers))
print(numbers2, type(numbers2))
print(mixed, type(mixed))

matrix = [
    ["blue", "is", "the", "best"],
    ["lucky", "number", "seven"],
    ["the", "flame", "of", "hope", "solaris"]
]
mixed_matrix = [
    [1, 2, 3],
    ["one", "two", "three"],
    [True, True, True],
    [1, "two", True]
]

print(matrix, type(matrix))
print(mixed_matrix, type(mixed_matrix))