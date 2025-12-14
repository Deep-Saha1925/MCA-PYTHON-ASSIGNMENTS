# l = input("Enter list: ").split()
l = [1, 2, 3, 1, 2, 3, 4, 1, 2]
# l = [1,2,3]
newList = []

for i in range(len(l)):
    x = l[0:i] + l[i+1:]
    if x not in newList:
        newList.append(x)

print(newList)