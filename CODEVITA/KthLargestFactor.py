n, k = map(int, input("Enter n, k: ").split())

a = 1
for i in range(n, 0, -1):
    if n % i == 0:
        k -= 1
    if k == 0:
        a = i
        break

print(a)
        