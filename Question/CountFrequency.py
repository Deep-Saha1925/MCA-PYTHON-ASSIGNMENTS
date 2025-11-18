s = input("Enter a string: ").lower()
vis = ""
for ch in s:
    vis += ch
    if vis.count(ch) > 1 or ch == ' ':
        continue
    count = s.count(ch)
    print(ch, ":", count)
    
print(vis)