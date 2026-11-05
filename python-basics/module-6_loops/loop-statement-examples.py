# Example 1
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
working_days = ""
first_working_day = 0
last_working_day = 4

for i in range(len(days)):
    if not(first_working_day <= i <= last_working_day):
        continue
    working_days += days[i][0].upper() + days[i][1:]
    if i != last_working_day:
        working_days += ", "

print("The working days are:", working_days + "\n")

# Example 2
emails = [
    "hey@seven.com",
    "hey@gian-i.media",
    "my-g@the-boss",
    "TO ARMS;",
    "hey@blue.com"
]

for email in emails:
    if ";" in email:
        print(f"Unsafe data \"{email}\" detected! Likely SQL Injection. Terminating program.")
        break
    if email.count("@") != 1 or email.count(".") != 1:
        print(f"Email: {email} is not an acceptable format")
        continue

    print(f"Verified email: {email}")