s1 = input("Enter string1: ").split()
s2 = input("Enter string2: ").split()

for w in s1:
    if w not in s2:
        print(w)

for w in s2:
    if w not in s1:
        print(w)