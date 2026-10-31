dateFormat1 = "2026/05/10"
print(dateFormat1)

dateFormat2 = dateFormat1.replace("/", "-")
print(dateFormat2)

price = "1234,56"
print(price.replace(",", "."))

phone = "416-671-5765"
print(phone.replace("-", ""))

price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))

phone_number = "+49 (176) 123-4567"
print(
    phone_number.replace("+", "")
    .replace(" ", "")
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
)
