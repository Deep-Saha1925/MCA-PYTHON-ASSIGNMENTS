n = int(input("Enter no. of values"))
even_sum = 0    # calculate even sum
odd_sum = 0     # calculate odd sum
for i in range(n):
    num = int(input("Enter no.: "))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
        
print("Even sum: ", even_sum)
print("Odd sum: ", odd_sum)