def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

a = int(input("Enter no: "))
print("Factorial:", fact(a))