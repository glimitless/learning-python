text = " Max "
print(text.lstrip().rstrip())
print(text.strip())

text = "Software Engineering".strip()
print(text)

text = "  ###I## want# to be####a Design### Engineer#### ".strip("# ")
print(text + "\n")

text = "  Engineering"
is_clean = len(text) == len(text.strip())
print(f"Number of spaces: {len(text) - len(text.strip())}")
print(f"Is my data clean? {is_clean}")
