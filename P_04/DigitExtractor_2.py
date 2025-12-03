s = input("Enter string: ")

l = []
summ = 0
avg = 0
maximum = -1
f = True

for ch in s:
    if ch.isdigit():
        dig = ord(ch)-48
        l.append(dig)
        f = False
  
if f:
    print("No digit in String")
else:
    minimum = l[0]
            
    for el in l:
        summ += el
        maximum = max(maximum, el)
        minimum = min(minimum, el)
        
    print("Sum: ", summ)
    print("Average: ", summ/len(l))
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)