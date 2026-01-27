l = []
c = 0
s = 0
with open("input.txt", "r") as file:
    for f in file:
        c += 1
        l.append(int(f))
        s += int(f)
        
d = {
    "count": c,
    "Sum": s
}
with open("output.txt", "w") as file:
    file.write(f'{c} input items.\nSum = {s}\n{l}\n{d}')