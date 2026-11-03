score = None

while not score:
    score_input = input("Enter the student's result on their paper (0-100): ").strip()
    if score_input.isnumeric() and int(score_input) <= 100 and int(score_input) >= 0:
        score = int(score_input)
        print()
    else:
        print("Please enter a valid score\n")

result = "pass" if score >= 75 else "fail"
print(f"The student {result}ed.")