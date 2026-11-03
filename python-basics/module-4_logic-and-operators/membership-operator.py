guardians = ["solaris", "terra", "blue"]

print("blue" in guardians, "blue" not in guardians)
print("b" in guardians[2])

domain = "gmail.com"
trusted_domains = ["gmail.com", "outlook.com", "yahoo.com"]

if domain in trusted_domains:
    print("we trust you")
else:
    print("we don't trust you")