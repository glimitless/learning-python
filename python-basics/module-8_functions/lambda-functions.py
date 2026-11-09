data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data_1 = filter(lambda x: x <= 5, data)
threshold = lambda x: x <= 5
filtered_data_2 = filter(threshold, data)
print(data)
print(list(filtered_data_1))
print(list(filtered_data_2))

add = lambda x, y: x + y
print(add(2, 3))

check = lambda i: i in data
print(check(12))