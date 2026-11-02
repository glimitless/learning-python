x = 7  # int
y = 7.2  # float
z = 3 + 4j  # complex
text1 = "21"
text2 = "24.7"

real = 3
imaginary = 4

print(type(x), type(y), type(z))
print(text1, type(text1), type(int(text1)), int(text1) * 3)
print(y, int(y), x, float(x), float(text2), type(float(text2)))
print(complex(real, imaginary), type(complex(real, imaginary)))
