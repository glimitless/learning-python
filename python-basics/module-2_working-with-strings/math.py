password = "123awawdawdawdawd"
print(len(password))

if len(password) < 8:
    print("Your password is too short")
else:
    print("Your password is a good length")

text = """
Python is easy to learn.
Python is powerful.
Many people love Python.
"""

print(text.count("Python"))
