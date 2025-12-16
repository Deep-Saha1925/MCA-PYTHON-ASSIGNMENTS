dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}

for d in dic2:
    if d not in dic1:
        dic1[d] = dic2[d]
        
print(dic1)