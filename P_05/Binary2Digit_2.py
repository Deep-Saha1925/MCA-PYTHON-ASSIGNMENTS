digs = input("Enter binary digit: ")
val = 0
length = len(digs)-1
res = 0
for ch in digs:
    val = ord(ch)-48
    res += val*(2**length)
    length-=1

print(res)