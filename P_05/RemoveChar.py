s = input("Enter string: ")
i = int(input("Enter index to remove: "))

s1 = s[:i]+s[i+1:]
print(s1)