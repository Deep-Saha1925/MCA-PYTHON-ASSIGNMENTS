s = input("Enter sentence: ")
k = int(input("Enter k: "))
words = s.split()

for w in words:
    if len(w) > k:
        print(w)