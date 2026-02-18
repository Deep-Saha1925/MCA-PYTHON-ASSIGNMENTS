test1 = {
    'pl1': 12,
    'pl2': 28,
    'pl3': 20
}

test2 = {
    'pl1': 10,
    'pl3': 5,
    'pl4': 45
}

t3 = {}
m_n = ""
m_v = 0

for k in test1.keys():
    if k not in t3:
        t3[k] = test1[k]
    else:
        t3[k] += test1[k]
        
for k in test2.keys():
    if k not in t3:
        t3[k] = test2[k]
    else:
        t3[k] += test2[k]
        
for k in t3.keys():
    if t3[k] > m_v:
        m_v = t3[k]
        m_n = k
        
print(t3)
print(m_n)