s = input("Enter string: ")
min_char = s[0]
min_count = s.count(s[0])

for ch in s:
    c = s.count(ch)
    if c < min_count:
        min_count = c
        min_char = ch

print("Least frequent:", min_char)