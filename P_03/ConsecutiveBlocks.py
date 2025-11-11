# Take 8 integers as input using loop
print("Enter 8 integers:")

block_count = 0
current_length = 1
longest = 1

# Take the first number separately
prev = int(input())
count = 1  # to track how many numbers read

while count < 8:
    num = int(input())
    count += 1

    if num > prev:
        current_length += 1
    else:
        block_count += 1
        if current_length > longest:
            longest = current_length
        current_length = 1

    prev = num

# Handle last block
block_count += 1
if current_length > longest:
    longest = current_length

print("Number of increasing blocks:", block_count)
print("Length of the longest block:", longest)