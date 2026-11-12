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

print(clean_and_split_email(' hey@GIAN-i.media '))