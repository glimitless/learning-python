text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

search = "Blue's World".strip().lower()
data = "blue's world"

print(search == data)

userInput = "968-Maria, ( D@t@ Engineer );; 27y  "
cleanedInput = userInput.strip()
print(cleanedInput)

name = cleanedInput[4:9]
role = cleanedInput[13:26].lower().replace("@", "a")
age = cleanedInput[-3:-1]

print(f"name: {name} | role: {role} | age: {age}")
