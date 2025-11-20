s = input("Enter string: ")
max_char = s[0]
max_count = s.count(s[0])

for ch in s:
    c = s.count(ch)
    if c > max_count:
        max_count = c
        max_char = ch

print("Max frequent:", max_char)