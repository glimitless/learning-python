# Example 1
colors = ["red", "blue", "green"]
sizes = ["large", "medium", "small"]

for color in colors:
    for size in sizes:
        print(color + ": Size - " + size)

years = [2029, 2030]
months = ["Jan", "Feb"]
days = range(1, 29)

print("\n" + "*"*32 + "\n")

# Example 2
for year in years:
    for month in months:
        for day in days:
            if year == 2030 and month == "Feb" and day == 7:
                print("End of the beginning. Beginning of the end.")
                continue
            print(f"report_{year}_{month}_{day}")

print("\n" + "*"*32 + "\n")

# Example 3
tables = ["customers", "orders", "products", "prices"]
columns = ["id", "creation_date"]

for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL")
