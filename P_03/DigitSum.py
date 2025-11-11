def add_digit(num):
    add = 0
    while num > 0:
        add += num % 10
        num = num // 10
    return add

count = 0  # To count how many positive numbers processed

while True:
    num = int(input("Enter a positive integer (0 or negative to stop): "))
    
    if num <= 0:
        break  # Stop if 0 or negative
    count += 1

    iterations = 0
    digit_sum = num

    # Keep finding digit sum until it becomes a single digit
    while digit_sum > 9:
        digit_sum = add_digit(digit_sum)
        iterations += 1

    print("Iterations:", iterations, ", Final digit:", digit_sum)

print("Total numbers processed:", count)