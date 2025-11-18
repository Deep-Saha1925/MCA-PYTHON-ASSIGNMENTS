s = input("Enter a string: ").lower()
res = ""
for ch in s:
    if ch in 'aeiou':
        res += chr(ord(ch)+1)
    else:
        res += ch
    
print(res)