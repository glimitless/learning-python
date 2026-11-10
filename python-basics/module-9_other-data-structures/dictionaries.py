guardian = {
    'name': 'Blue',
    'elements': [
        'Light',
        'Chance',
        'Color'
    ],
    'age': 23
}
print(guardian)
print(guardian['elements'], guardian.get('elements'), guardian.get('girlfriend'), guardian.get('girlfriend', 'One day'))
print('age' in guardian, 'age' not in guardian)
print(guardian.keys(), guardian.values(), guardian.items())
print()

for aspect in guardian:
    print(aspect)
else:
    print()

for aspect, value in guardian.items():
    print(aspect, value)
else:
    print()

guardian['weapon'] = 'Sword of Justice'
guardian['age'] = 24
print(guardian)
print()

guardian.update({'hobbies': ['building', 'designing', 'dreaming'], 'age': 23})
print(guardian)
print()

age = guardian.pop('age')
print(age, guardian.pop('girlfriend', 'key-not-found'))
print(guardian)
print()

guardian.popitem()
print(guardian)