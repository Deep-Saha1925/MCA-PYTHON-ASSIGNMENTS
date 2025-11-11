n = int(input("Enter no. of values"))
k = int(input("Enter k: "))
first = True
numbers = ""
for i in range(n):
    num = int(input("Enter no.: "))
    if num % k == 0:
        if first:
            first = False
            continue
        numbers = numbers + str(num) + " "
        
print(numbers)