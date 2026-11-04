for i in (1, 2, 3, 4, 5):
    print(i)
    if i == 2:
        break

print("loop has finished\n")

message = None
invalid_numbers = ("2", "3", "4", "5", "6", "7", "8", "9")

while not message:
    message_input = input("Enter a message: ").lower().strip()

    if message_input == "quit" or message_input == "q":
        break

    if not message_input.isnumeric():
        print("Only binary messages are allowed.\n")
    elif any(number in message_input for number in invalid_numbers):
        print("Only binary messages allowed\n")
    else:
        message = message_input

if message:
    print(f"Understood. Excecuting instructions: {message}")
else:
    print("See you later.")
    