# Input from user
original_string = input("Enter the original string: ")
substring = input("Enter the substring to find: ")

try:
    position = original_string.index(substring)
    print("First occurrence is at index:", position)
except ValueError:
    print("Substring not found.")