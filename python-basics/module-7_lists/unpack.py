personal_info = ['Blue', '27', ['Designer', 'Software Engineer', 'Founder'], 'Canada']

name, age, role, country = personal_info
ego, *details, location = personal_info
important, *not_important = personal_info
*not_important2, important2 = personal_info
important3, *_, important4 = personal_info

print(name, age, role, country)
print(ego, details, location)
print(important, not_important)
print(not_important2, important2)
print(important3, important4)
print()

data = ["Sword of Justice", "Light", "Hero", "I Summon Thee"]
item, _, calling, _ = data 
print(item, calling)