import random

score = random.randint(0, 100000)
user = "blue"
print("score:", str(score) + "\n")

if score == 7:
    print("single luck.")
    if user == 'blue':
        print("Not so lucky today eh blue.")
    else:
        print("Not too bad a result in the grand scheme of things.")
elif score == 77:
    print("double luck.")
    if user == 'blue':
        print("I've seen better, especially from you blue.")
    else:
        print("Congrats.")
elif score == 777:
    print("triple luck.")
    if user == 'blue':
        print("Not bad.")
    else:
        print("Nice job.")
elif score == 7777:
    print("quadruple luck.")
    if user == 'blue':
        print("...")
    else:
        print("Nice job!")
elif score == 77777:
    print("quintuple luck.")
    if user == 'blue':
        print("ugh.")
    else:
        print("OH MY GOD, CONGRATULATIONS! You rolled the quintuple luck!")
else:
    print("no luck ;(")
    if user == 'blue':
        print("HAHAHAHAHA. You suck blue.")
    else:
        print("Better luck next time!")

if user == "blue":
    print("\n[insert-chance-multiplier]")
