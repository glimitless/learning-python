price_shirt = 25.00
qty_shirt = 2

price_jeans = 45.00
qty_jeans = 1

total_shirt = price_shirt * qty_shirt
total_jeans = price_jeans * qty_jeans
subtotal = total_shirt + total_jeans
discount = subtotal * 0.10
final_total = subtotal - discount
split_amongst_friends = final_total / 3

print(
    "The amount each of you will have to pay is $"
    + str(split_amongst_friends)
    + " USD."
)

print("$", final_total % 3, "dollars less and it could've divide evenly, oh well.")
