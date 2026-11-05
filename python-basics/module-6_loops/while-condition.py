import random

counter = 1
jackpot = False
ultimate_jackpot = False

print("You got 100 chances to get lucky")
while counter <= 100:
    spin1 = random.randint(1,10)
    spin2 = random.randint(1,10)
    spin3 = random.randint(1,10)
    if spin1 == spin2 and spin2 == spin3:
        message = f"ULTIMATE JACKPOT BABY! [{spin1}][{spin2}][{spin3}]\n" if spin1 == 7 else f"JACKPOT BABY! [{spin1}][{spin2}][{spin3}]\n"
        if spin1 == 7:
            ultimate_jackpot = True
        else:
            jackpot = True
        print(message)
        break
    print(f"Roll #{counter}: Unsuccessful. Result: [{spin1}][{spin2}][{spin3}]")
    counter += 1
else:
    print("You were not lucky after 100 rolls. Better luck next time!")

if ultimate_jackpot:
    action_made = None
    while not action_made:
        action = input("You've just been given the power to change the world. What would you like to do? ").strip()
        if not action or action.lower() in ("none", "nothing"):
            print("Unfortunately, you must do something.\n")
            continue
        print("An all-encompassing flash of light emerges from the glowing dice. As it subsides, you notice the world has been changed according to your desire.")
        print("Thanks for playing!")
        action_made = True
elif jackpot:
    quit_jackpot = False
    while not quit_jackpot:
        action = input("Your energy output spikes. From all appearances it looks to be boundless.\nA simple command of \"quit\" or \"release\" ends the jackpot.\nWhat do you wish to do: ")
        if action in ("quit", "release"):
            quit_jackpot = True
            print("Thanks for playing!")
            continue
        print("An action has been made. It's result is dependant on your own ability.\n")
