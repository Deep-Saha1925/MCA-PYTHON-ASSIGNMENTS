s1 = input("Enter string: ")
s2 = input("Enter string: ")

def findLength(s):
    c = 0
    for ch in s:
        c += 1
        
    return c

newstr = ""
l = min(findLength(s1), findLength(s2))

for i in range(l):
    newstr += s1[i] + s2[findLength(s2) - i - 1]
    
if findLength(s1) > findLength(s2):
    newstr += s1[findLength(s2):]
elif findLength(s2) > findLength(s1):
    newstr += s2[findLength(s2)-findLength(s1)-1::-1]
    
print(newstr)