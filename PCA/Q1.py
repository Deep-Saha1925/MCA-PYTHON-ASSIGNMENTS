s = input()+' '
spl = input()
j = input()
x=0
l=[]
for ch in range(len(s)):
    if s[ch] == spl:
        l.append(s[x:ch])
        x = ch+1
        
print(l)
newStr = ""
for wrd in l:
    newStr += wrd + j
    
print(newStr[:-1])