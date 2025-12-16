s = 'MCA1stsem'.lower()
d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 0
        
print(d)