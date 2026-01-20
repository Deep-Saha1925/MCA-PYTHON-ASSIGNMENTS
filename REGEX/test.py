import re

word = "Siliguri institute of technology MCA 1st semester 2025 odd"

match = re.search("institute", word)
print(match)

# digits
match = re.findall("[0-9]", word)
print(match)

# Single digit
match = re.search("[0-9]{1}", word)
print(match)

# multiple digit
match = re.findall("[0-9]{2,4}", word)
print(match)

# 2024/2025
match = re.findall("202[4-5]", word)
print(match)