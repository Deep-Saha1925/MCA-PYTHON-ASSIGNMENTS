def reverse(s):
    newS = ""
    for c in s:
        newS = c + newS
        
    return newS

s = input("Enter string: ")
print("Reverse:", reverse(s))