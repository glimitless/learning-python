# Example 1
names = ["Blue", "Seven", None, "Gian-I"]
names_output = ""

for name in names:
    if not name:
        print("Found missing name value. Terminating program.\n")
        break
    names_output += name
    if name != names[len(names) - 1]:
        names_output += ", " 
    print("Name:", name)
else:
    print(f"All names: {names_output}\n")

# More for loops practice
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
    # "TO ARMS;",
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
else:
    print("Successfully looped through full dataset.\n")

# Example 3 (Sorta)
files = ["blues-world.csv", "report.csv", "other.csv", "cost-range.pdf", "magic-numbers.csv"]
all_files_csv = None

for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a .csv file.")
        if all_files_csv is None:
            all_files_csv = False
        continue
if all_files_csv is None:
    print("All files are .csv")
else:
    print("Not all files are .csv")
