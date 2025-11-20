target = input("Enter target: ")
attempt = ""
attempts = 0

while attempt != target:
    attempt = input("Enter guess: ")
    attempts += 1

print("Matched in", attempts, "attempts")