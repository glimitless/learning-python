letters = ['c', 'e', 'f', 'd', 'j', 'g', 'i', 'h', 'b', 'a']
ascending_list = sorted(letters)
descending_list = sorted(letters)
print(letters, ascending_list, descending_list)
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)