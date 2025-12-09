a = input("Enter a:").upper()
b = input("Enter b:").upper()

def isSubSet(a, b):
    missing = []
    c = 0

    for ch in a:
        if ch not in b:
            missing.append(ch)
            c += 1
    print(c)

    if len(missing) == 0:
        print(True)
    else:
        print(False)
        print("Missing characters:", missing)

x = str(set(a))
y = str(set(b))

isSubSet(x, y)