d = {
    'Cierra Vega': 175,
    'Alden Cantrell': 180,
    'Kierra Gentry': 165,
    'Pierre Cox': 190,
}

newD = {}

for k in d.keys():
    if d[k] > 170:
        newD[k] = d[k]
        
print(newD)