email = None
password = None

while not email:
    email_input = input("Please enter your company email (.com, .org, or .net): ").lower().strip()

    if not ("@" in email_input and "." in email_input) and email_input.count("@") != 1:
        print("Invalid email format.\n")
    elif not email_input.endswith((".com", ".net", ".org")):
        print("Invalid top-level domain. Must be a company email.\n")
    elif len(email_input) > 254:
        print("Email exceeds 254 character limit.\n")
    elif not (email_input[0].isalnum() and email_input[len(email_input) - 1].isalnum()):
        print("Email must start and end with either a letter or digit.\n")
    else:
        print("Thank you \n")
        email = email_input

while not password:
    password_input = input("Please enter a password for your account: ").strip()
    if len(password_input) < 8:
        print("Password must be greater than 8 characters.\n")
    elif password_input == password_input.lower():
        print("Password must include at least 1 uppercase character.\n")
    elif password_input == password_input.upper():
        print("Password must contain at least 1 lowercase character.\n")
    elif password_input == email:
        print("Password cannot be same as email.\n")
    elif " " in password_input:
        print("Password cannot contain spaces.\n")
    elif not (password_input[0].isalnum() and password_input[len(password_input) - 1].isalnum()):
        print("Password must start and end with either a letter or digit.\n")
    else:
        print("Thank you.\n")
        password = password_input

print(f"Your email is {email} and your password is {password}.")
