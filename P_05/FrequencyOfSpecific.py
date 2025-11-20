lst = ["apple", "banana", "mango"]
ch = input("Enter character: ")
count = 0

for word in lst:
    count += word.count(ch)

print("Frequency:", count)