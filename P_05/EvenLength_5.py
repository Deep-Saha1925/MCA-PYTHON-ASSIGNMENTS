s = input("Enter string: ")
for w in s.split():
    if len(w) % 2==0:
        print(w)