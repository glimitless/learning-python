prices = ['$77.77', '$12.50', '$9.99', '$100.00']

convert_price_to_float = lambda price: float(price.replace('$', ''))

float_prices = list(map(convert_price_to_float, prices))
for price in float_prices:
    print(type(price), isinstance(price, float), price)
else:
    print()

print("Prices under $50")
for price in filter(lambda p: p < 50.00, float_prices):
    print(price)
else:
    print()
