def write_log(message):
    with open(r'C:\Users\gianc\Downloads\app.log', 'a') as file:
        file.write(message + '\n')

def clean_and_split_email(email: str):
    cleaned = email.strip().lower()
    username, domain = cleaned.split('@')
    # at_symbol_index = cleaned.find('@')
    # username = cleaned[:at_symbol_index]
    # domain = cleaned[at_symbol_index + 1:]

    return {
        'email': cleaned, 
        'username': username, 
        'domain': domain
    }

def is_valid_email(email: str):
    return '@' in email and '.' in email

def process_user_email():
    run_program = True
    cleaned_email = ''
    write_log(f'Application started.')
    while run_program:
        email = input('Please enter your email: ')

        if not is_valid_email(email):
            write_log(f'Invalid email received: {email}')
            print()
            continue
        else:
            cleaned_email = email = clean_and_split_email(email)
            write_log(f'Processed email: {email}')
            run_program = False
    write_log('Application Terminated.')
    return cleaned_email

email = process_user_email()

    
    