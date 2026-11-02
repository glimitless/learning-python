username = "blue"
password = "blueisthebest"

access_granted = False

while (
    access_granted == False
    and (username_input := input("Enter username: ")).lower().strip() != "quit"
    and (password_input := input("Enter password: ")).lower().strip() != "quit"
):
    if username_input == username and password_input == password:
        access_granted = True
    else:
        print("invalid credentials \n")

if access_granted == True:
    print("Access Granted")
else:
    print("See you later")
