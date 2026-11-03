quit_check = False
username = None
email = None
password = None
age = None
admin_users = ["blue-rocks", "gian-i", "lucky-seven"]
banned_users = ["not-cool-stuff", "even-worse"]
verified_emails = ["hey@blue.com", "example@example.com"]

while not age and not quit_check:
    age_input = input("Enter your age: ").lower().strip()

    if age_input.lower() == "quit":
        quit_check = True
    elif not age_input.isnumeric():
        print("Only numbers please.\n")
    elif int(age_input) >= 18:
        print("This platform is for children. You are either 18 years old or older.")
        quit_check = True
    else:
        print("Nice.\n")
        age = age_input

while not username and not quit_check:
    username_input = input("Enter your username: ").strip()
    if username_input.lower() == "quit":
        quit_check = True
    elif username_input in banned_users:
        print("You are banned.\n")
        quit_check = True
    elif " " in username_input:
        print("No spaces please.\n")
    elif username_input != username_input.lower():
        print("Only lowercase letters please.\n")
    elif len(username_input) <= 5:
        print("Username must be longer than 5 characters.\n")
    elif username_input in admin_users:
        print("Hello admin.\n")
        username = username_input
    else:
        print("Nice.\n")
        username = username_input

while not email and not quit_check:
    email_input = input("Enter your email: ").lower().strip()
    if email_input == "quit":
        quit_check = True
    elif not email_input:
        print("Invalid: Blank Response.\n")
    elif "@" not in email_input:
        print("Missing @ character.\n")
    elif not email_input.endswith(".com"):
        print("Only commercial entities are allowed on this platform. Please enter a .com email address.\n")
    elif email_input not in verified_emails:
        print("Be sure to verify your email.")
        email = email_input
    else:
        print("You're email is verified. Nice.\n")
        email = email_input

while not password and not quit_check:
    password_input = input("Enter your password: ").strip()
    if password_input.lower() == "quit":
        quit_check = True
    elif " " in password_input:
        print("No spaces please.\n")
    elif len(password_input) < 8:
        print("Your password must be at least 8 characters long.\n")
    else: 
        print("Nice.\n")
        password = password_input

if quit_check:
    print("See you later.")
else:
    print(f"Username: {username}, email: {email}, age: {age}. Welcome to the platform.")
