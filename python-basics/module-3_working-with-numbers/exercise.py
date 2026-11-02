import random

random_number = random.randint(1, 100)
print(f"Your random number is {random_number}")
if random_number % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")
