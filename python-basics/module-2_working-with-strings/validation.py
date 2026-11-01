country = "USA"
print(country, country.isalpha())

phone = "+1-647-123-1234"
print(phone, phone[phone.find("-") + 1 :].replace("-", "").isnumeric())
