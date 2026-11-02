print(bool(0), bool(1), bool(7), bool(""), bool("Hello"), bool(None))

email = "hey@blue.com"
phone = ""
username = "blue"
print(any([username, phone, email]))
print(all([username, phone, email]))
print(isinstance(email, str), isinstance(phone, int))
print("@" in email, email.startswith("hey"), email.endswith(".com"))
