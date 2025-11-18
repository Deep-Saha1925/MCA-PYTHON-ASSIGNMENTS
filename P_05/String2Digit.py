digs = input("Enter digit: ")
val = 0
for ch in digs:
    val = val*10+(ord(ch)-48)

print(val)