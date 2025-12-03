a = input("Enter string a: ")
b = input("Enter string b: ")

missing = []

for ch in a:
    if ch not in b:
        missing.append(ch)

if len(missing) == 0:
    print(True)
else:
    print(False)
    print("Missing characters:", missing)