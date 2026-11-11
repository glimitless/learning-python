case_rule = 'lower'
def clean_string(string: str):
    cleaned = string.strip();
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    return cleaned

def computer_message(message: str):
    cleaned = clean_string(message)
    print(f'Computer says: "{cleaned}"')

def user_prompt(prompt: str):
    cleaned = clean_string(prompt)
    print(f'Computer asks: "{cleaned}"')
    return input("What would you like to respond? ").strip().lower()

def computer_response(response: str):
    cleaned = clean_string(response)
    print(f'Computer responds: "{cleaned}"')

computer_message("Good morning.")
response_1 = user_prompt("How was your day?")
print()

computer_response('Interesting...')

