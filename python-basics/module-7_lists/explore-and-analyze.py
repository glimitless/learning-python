numbers = [1, 2, 4, 7, 3, 4, 5, 6]
numbers2 = [1, 2, 4, 7, 3, 4, 5, 6]
numbers3 = numbers
list_1 = [7, 7, 7]
list_2 = [7, 7, 2]
values = ["good", "great", "awesome", "outstanding", "", "outstanding", "amazing"]

print(numbers)
print(f"max: {max(numbers)}, min: {min(numbers)}, sum: {sum(numbers)}, length: {len(numbers)}")
print(f"all: {all(numbers)}, any: {all(numbers)}")
print(f"count 5: {numbers.count(5)}, index 5: {numbers.index(5)}")
print(f"8 in: {8 in numbers}, 8 not in: {8 not in numbers}")
print()

print("nlist 1:", numbers)
print("nlist 2:", numbers2)
print("nlist 3:", numbers3)
print(f"nlist 1 == nlist 2: {numbers == numbers2}, nlist 1 is nlist 2: {numbers is numbers2}")
print(f"nlist 1 == nlist 3: {numbers == numbers3}, nlist 1 is nlist 3: {numbers is numbers3}")
print()

print("list_1:", list_1)
print("list_2:", list_2)
print(f"list_1 > list_2: {list_1 > list_2}, list_1 < list_2: {list_1 < list_2}")
print()

print(values)
print(f"all: {all(values)}, any: {any(values)}")
print(f"count \"outstanding\": {values.count("outstanding")}, index \"outstanding\": {values.index("outstanding")}")
print(f"\"outstanding\" in: {"outstanding" in values}, \"outstanding\" not in: {"outstanding" not in numbers}")