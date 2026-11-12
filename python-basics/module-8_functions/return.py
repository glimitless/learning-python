def character_select(input: str=None):
    if input:
        input = input.strip().lower()
        match input:
            case 'blue':
                selection = {
                    'name': 'Blue',
                    'age': 23,
                    'elements': [
                        'Light',
                    ],
                    'skills': [
                        'Swordmanship'
                    ],
                    'occupation': 'Royal Knight'
                }
            case 'seven':
                selection = {
                    'name': 'Seven',
                    'age': 27,
                    'elements': [
                        'Chance',
                    ],
                    'skills': [
                        'Gambling',
                        'Melee Combat'
                    ],
                    'occupation': 'Outlaw'
                }
    else:
        selection = None

    return selection

print(character_select(' SeVeN  '))

    