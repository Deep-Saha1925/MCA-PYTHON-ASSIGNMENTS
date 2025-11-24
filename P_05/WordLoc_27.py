s = input("Enter sentence: ").lower()
word = input("Enter word: ").lower()

index = s.find(word)

if index != -1:
    print(f"Word found at index: {index}")
else:
    print("Word not found in the string.")