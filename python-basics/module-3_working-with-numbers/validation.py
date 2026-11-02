x = 7.0
y = "7.7"
print(x, x.is_integer(), isinstance(x, str), isinstance(x, int), isinstance(x, float))
print(
    y,
    float(y).is_integer(),
    isinstance(y, str),
    isinstance(y, int),
    isinstance(y, float),
)
