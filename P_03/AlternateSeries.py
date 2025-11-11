n = int(input("Enter no. of values"))
even = True
numbers = ""
for i in range(n):
    num = int(input("Enter no.: "))
    if even:
        if num % 2 == 0:
            numbers = numbers + str(num) + " "
            even = False
    else:
        if num % 2 != 0:
            numbers = numbers + str(num) + " "
            even = True
        
print(numbers)