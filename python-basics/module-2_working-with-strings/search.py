date = "2026-Feb-10"
print(date.startswith("2026"))
print(date.endswith("10"))
print("Feb" in date)
print(date.find("Feb"))
print()

phone1 = "+49-176-12345"
phone2 = "+1-647-123-1234"
phone3 = "+1-868-654-3210"
area_code_to_check = "+49"
print(phone1[phone1.find("-") + 1 :], phone1.startswith(area_code_to_check))
print(phone2[phone2.find("-") + 1 :], phone2.startswith(area_code_to_check))
print(phone3[phone3.find("-") + 1 :], phone3.startswith(area_code_to_check))


email = "hey@blue.com"
is_google = email.endswith("gmail.com")
is_valid_email = "@" in email
print(is_valid_email, is_google)

file = "blue-manifesto.pdf"
is_pdf = file.endswith(".pdf")
print(is_pdf)

url = "https://blue.company.com/world/manifesto"
print("/blue" in url)
