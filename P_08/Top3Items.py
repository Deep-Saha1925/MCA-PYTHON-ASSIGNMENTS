d1={'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}
l = []
m = 0

for d in d1:
    l.append(d1[d])
    
l.sort(reverse=True)
l = l[:3]

for d in d1:
    if d1[d] in l:
        print(d, ":", d1[d])