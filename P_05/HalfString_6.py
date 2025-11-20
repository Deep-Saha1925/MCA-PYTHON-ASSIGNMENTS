# Uppercase half string
s = input("Enter string: ")
s1 = s[:len(s)//2] + s[len(s)//2::].upper()
print(s1)