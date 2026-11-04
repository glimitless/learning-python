scores = [77, 80, 75, 60, 42, 26, 73, 90]
total = 0

for score in scores:
    print(f"{total} + {score} = {total + score}")
    total += score

print("Total of scores:", total)