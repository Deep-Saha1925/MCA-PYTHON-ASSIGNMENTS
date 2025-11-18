s = input("Enter string: ")
res = ""
for wrd in s.split():
    res += wrd[:-1].capitalize() + wrd[-1].capitalize() + " "
    
print(res)