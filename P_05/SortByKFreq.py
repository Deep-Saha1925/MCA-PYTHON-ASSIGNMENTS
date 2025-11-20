lst = ["apple", "banana", "grape", "kiwi"]
k = int(input("Enter K: "))

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i].count(lst[i][k]) > lst[j].count(lst[j][k]):
            lst[i], lst[j] = lst[j], lst[i]

print(lst)