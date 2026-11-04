for i in (1, 2, 3, 4, 5, 6, 7, "etc"):
    print(f"Round: {i}")

cities = ("Chicago", "Toronto", "New York", "Jacksonville")
cities_output1 = ""
cities_output2 = ""

for city in cities:
    cities_output1 += city
    if city != cities[len(cities) - 1]:
        cities_output1 += ", "
print(cities_output1)

for i in range(len(cities)):
    cities_output2 += cities[i]
    if i != len(cities) - 1:
        cities_output2 += ", "
print(cities_output2)

for letter in "SEVEN":
    print(letter)

message = "lucky number seven"
message_output = ""
for index in range(2,len(message),2):
    message_output += message[index]
print(message_output)