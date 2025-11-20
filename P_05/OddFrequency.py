s = input("Enter string: ")
for ch in s:
    if s.count(ch) % 2 == 1:
        print(ch)