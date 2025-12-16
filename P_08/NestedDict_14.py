l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]
ans = []

for i in range(len(l1)):
    x = {}
    d = {}
    x[l2[i]] = l3[i]
    d[l1[i]] = x
    ans.append(d)
    
print(ans)