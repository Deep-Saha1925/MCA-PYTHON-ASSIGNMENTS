t = int(input("Enter no. of samples: "))
n = int(input("Enter n: "))

l = list(map(int, input("Enter samples: ").split()))

a = 0
x = l[0]
for i in range(1, n):
    x += l[i]
    a += x
    
print(a)