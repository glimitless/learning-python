letters = ['s', 'e', 'v', 'e', 'n']
numbers = [1, 2, 3, 4, 5, 6, 7]
combined_list = letters + numbers
comnbined_nested_list = [letters, numbers]
combined_zip_list = zip(letters, numbers)
combined_zip_list_2 = zip(letters, numbers, 'lucky')
print(combined_list)
print(comnbined_nested_list)
print(combined_zip_list, list(combined_zip_list))
print(letters*2)
print()

letters.extend(numbers)
print(letters)
print(combined_zip_list_2, list(combined_zip_list_2))
