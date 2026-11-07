answer_count = 0
max_answers = 3
while answer_count < max_answers:
    answer = input("Do you agree (yes/no): ").lower().strip()
    if answer == "yes":
        print("Glad we're on the same page.")
        break
    answer_count += 1
    if answer_count != max_answers:
        print()
else:
    print("3 strikes, you are out.")