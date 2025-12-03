lst = ["apple", "banana", "mango", "grape"]
inp = input("Enter word: ")

for w in lst:
    if w[0] == inp[0]:
        print(w)
        
def findLength(s):
    c = 0
    for ch in s:
        c += 1
        
    return c

print(findLength("Hello World"))