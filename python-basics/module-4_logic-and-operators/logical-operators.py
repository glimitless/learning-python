value = 7
minimum = 10
threshold = 20

print((value <= threshold and value >= minimum) or value == 7)

cpu_usage = 70
memory_usage = 95
computer_threshold = 90
if cpu_usage > computer_threshold or memory_usage > computer_threshold:
    print("alert")

email = "hey@blue.com"
password = ""
if email and password:
    print("processing login")
else:
    if not email and password:
        print("missing email")
    elif email and not password:
        print("missing password")
    else:
        print("missing all input fields")
