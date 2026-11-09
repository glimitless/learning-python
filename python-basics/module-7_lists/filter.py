data = [
    'blue777',
    'sevenSolaris',
    'flame-of-hope',
    None,
    False,
    'myG',
    'hero',
    'the-best, the-goat, whatever you\'ll call me'
]

first_filter_pass = filter(None, data)
second_filter_pass = filter(str.isalpha, first_filter_pass)
print(list(second_filter_pass))