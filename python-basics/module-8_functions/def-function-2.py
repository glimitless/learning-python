import time

guardians = {
    'blue': {
        'name': 'Blue'
    },
    'solaris': {
        'name': 'Solaris'
    },
    'seven': {
        'name': 'Seven'
    }
}

def guardian_summon(request:str, affinity:str='none'):
    cleaned_request = request.strip().lower()
    cleaned_affinity = affinity.strip().lower()
    print(f'Your request "{cleaned_request}" has been heard.')
    print(f'Parsing through database for guardians compatible with the {cleaned_affinity} element...')
    time.sleep(2)
    if 'luck' in cleaned_affinity or 'chance' in cleaned_affinity:
        print('\nGuardian Seven stands before you.')
    elif 'light' in cleaned_affinity:
        print('\nGuardian Blue stands before you.')
    else:
        print('\nThe summon has failed.')

guardian_summon('I want to change the world.', 'Chance') # Positional arguments
print()
guardian_summon(affinity='light', request='I want to soar amongst the stars.') # Keyword arguments
print()
guardian_summon('I like trains.') # Default value