letters = ['s', 'e', 'v', 'e', 'n']
unicodes = []
uppercase_letters = []

for char in letters:
    unicodes.append(ord(char))
for unicode, letter in zip(unicodes, letters):
    print(f"code point: {str(unicode)}, letter: {letter}")
else:
    print()

for index, letter in enumerate(letters):
    uppercase_letters.append(letter.upper())
    unicodes[index] = ord(letter.upper())

for unicode, letter in zip(unicodes, uppercase_letters):
    print(f"code point: {str(unicode)}, letter: {letter}")




