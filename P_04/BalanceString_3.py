s1 = input("Enter string: ").lower()
s2 = input("Enter string: ").lower()
l=[]

for ch in s1:
    if ch not in s2:
        l.append(ch)
        
if len(l) == 0:
    print("True")
else:
    print("False.\nCharacters missing: ")
    for e in l:
        print(e)