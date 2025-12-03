l = input("Enter string: ").split()
test = ''
sorted_list = []
ans = []

for wrd in l:
    sorted_list.append(sorted(wrd))
    
for i in range(len(sorted_list)):
    x = []
    if sorted_list[i] in sorted_list:
        x.append(l[i])
        
    ans.append(x)
    
print(l)
print(sorted_list)
print(ans)