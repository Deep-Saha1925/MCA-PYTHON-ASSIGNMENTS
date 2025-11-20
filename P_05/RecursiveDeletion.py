s = input("Enter string: ")

while len(s) > 1 and s[0] == s[-1]:
    s = s[1:-1]

if s == "":
    print("Can become empty")
else:
    print("Cannot become empty")