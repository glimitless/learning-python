quit_messages = ("quit", "stop")

while True:
    user_input = input("The Pontifex says hello.\nWrite \"quit\" or \"stop\" to exit the program. \nHow do you respond? ").strip()

    if user_input.lower() in quit_messages:
        print("See you later")
        break
    print("Interesting...\n")