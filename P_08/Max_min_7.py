d1 = {1: 10, 2: 20, 4: 46, 3: 30, 5: 520, 6: 60}
maximum = d1[1]
minimum = d1[1]

for d in d1.keys():
    if d1[d] > maximum:
        maximum = d1[d]
    if d1[d] < minimum:
        minimum = d1[d]
        
print(minimum)
print(maximum)