list_numbers = [7, 77, 777]
print('Lists are')
print('\tordered:         ', list_numbers)
list_numbers.append(77)
list_numbers.append(7)
print('\tallow duplicates:', list_numbers)
list_numbers[3] = 444
print('\tmutable:         ', list_numbers)
print('\tindexed:             ', list_numbers[1])
print()

tuple_numbers = (7, 77, 777, 77, 7)
print('Tuples are')
print('\tordered:         ', tuple_numbers)
print('\tallow duplicates:', tuple_numbers)
print('\tnot mutable:     ', tuple_numbers)
print('\tindexed:             ', tuple_numbers[1])
print()

set_numbers = {7, 77, 777}
print('sets are')
print('\tnot ordered:     ', set_numbers)
print('\tno duplicates:   ', set_numbers)
set_numbers.remove(77)
set_numbers.add(444)
print('\tmutable:         ', set_numbers)
print('\tnot indexed:             ')
