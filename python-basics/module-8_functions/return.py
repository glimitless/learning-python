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
                character_id = input
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
                    'occupation': 'Outlaw',
                    'id': 'seven'
                }
                character_id = input
    else:
        selection = None
        character_id = ''

    return selection, character_id

print(character_select(' SeVeN  '))

    