s = input("Enter string: ")
rot = 0
temp = s

while True:
    temp = temp[1:] + temp[0]
    rot += 1
    if temp == s:
        break

print("Minimum rotations:", rot)