l = [
    [5, 3, 0, 2],
    [7, 0, 2, 1],
    [0, 1, 4, 0]
]

p1 = 0
p2 = 0
p3 = 0
p4 = 0
max_sales = 0
p_max = ""

for i, x in enumerate(l):
    print("Day", i+1, ":", end='')
    for j, y in enumerate(x):
        if j == 0:
            p1 += y
        elif j == 1:
            p2 += y
        elif j == 2:
            p3 += y
        elif j == 3:
            p4 += y
        print(" Product", j+1, "sold", y, end='')
    print()

if p1 > max_sales:
    max_sales = p1
    p_max = "Product 1"
if p2 > max_sales:
    max_sales = p2
    p_max = "Product 2"
if p3 > max_sales:
    max_sales = p3
    p_max = "Product 3"
if p4 > max_sales:
    max_sales = p4
    p_max = "Product 4"
    
min_sales = p1
p_min = ""
    
if p1 < min_sales:
    min_sales = p1
    p_min = "Product 1"
if p2 < min_sales:
    min_sales = p2
    p_min = "Product 2"
if p3 < min_sales:
    min_sales = p3
    p_min = "Product 3"
if p4 < min_sales:
    min_sales = p4
    p_min = "Product 4"

print("Max Sales: ", p_max)
print("Min Sales: ", p_min) 

print('---SUMMARY---')
print("Sales of Product 1: ", p1)
print("Sales of Product 2: ", p2)
print("Sales of Product 3: ", p3)
print("Sales of Product 4: ", p4)