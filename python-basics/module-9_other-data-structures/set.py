set_of_sevens = {7, 77, 777, 7777, 77777}
print(set_of_sevens)

set_of_sevens.add(777777)
print(set_of_sevens)

set_of_sevens.add(7)
print(set_of_sevens)

set_of_sevens.remove(7)
print(set_of_sevens)

tuple_of_eights = (8, 8, 88, 888)
set_of_sevens.update(tuple_of_eights)
print(set_of_sevens)

set_of_sevens |= {9, 99, 99, 9999, 99}
print(set_of_sevens)

for eight in tuple_of_eights:
    set_of_sevens.discard(eight)
else:
    print(set_of_sevens)