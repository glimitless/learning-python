def computer_message(message: str):
    print(f'Computer says: "{message}"')

def user_prompt(prompt: str):
    print(f'Computer asks: "{prompt}"')
    return input("What would you like to respond? ")

def computer_response(response: str):
    print(f'Computer responds: "{response}"')

computer_message("Good morning.")
response_1 = user_prompt("How was your day?")
print()

computer_response('Interesting...')
