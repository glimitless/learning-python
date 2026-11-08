letters = ['s', 'e', 'v', 'e']
letters.append('n')
letters_output = ""
for letter in letters:
    letters_output += letter
else:
    print(letters_output)

letters_2 = ['l', 'u', 'k', 'y']
letters_2.insert(2, 'c')
letters_2_output = ""
for letter in letters_2:
    letters_2_output += letter
else:
    print(letters_2_output + "\n")

letters.clear()
print("seven ->", letters)

letters_2.remove('c')
letters_2.pop(-1)
print("lucky ->", letters_2)