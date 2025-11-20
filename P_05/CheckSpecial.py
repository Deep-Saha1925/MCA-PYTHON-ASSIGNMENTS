s = input("Enter string: ")
flag = False

for ch in s:
    if not ch.isalnum():
        flag = True
        break

if flag:
    print("Contains special characters")
else:
    print("No special characters")