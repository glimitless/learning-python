username = "blue"
password = "blueisthebest"

access_granted = False
is_banned = False
is_guest = False

guest_check = False
guest_quit = False
while not (guest_check or guest_quit):
    is_guest_input = (
        input("Would you like to login as a guest? (Y/N): ").lower().strip()
    )
    if is_guest_input == "y":
        print("Welcome Guest")
        guest_check = True
        access_granted = True
    elif is_guest_input == "n":
        print("Ok\n")
        guest_check = True
    elif is_guest_input == "quit":
        guest_quit = True
    else:
        print("Invalid input\n")

while (
    not (is_banned or guest_quit or access_granted)
    and (username_input := input("Enter username: ")).lower().strip() != "quit"
    and (password_input := input("Enter password: ")).lower().strip() != "quit"
):
    if username_input == username and password_input == password:
        print("Welcome Blue")
        access_granted = True
    else:
        print("invalid credentials\n")

if is_banned == True:
    print("You are banned from using this platform")
elif access_granted == True:
    print("Access Granted")
else:
    print("See you later")
