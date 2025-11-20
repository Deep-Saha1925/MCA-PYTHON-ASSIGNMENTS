s = input("Enter string: ").lower()
vowels = "aeiou"
flag = True

for v in vowels:
    if v not in s:
        flag = False
        break

if flag:
    print("Contains all vowels")
else:
    print("Does not contain all vowels")