# def permute(s, ans=""):
#     if s == "":
#         print(ans)
#         return
#     for i in range(len(s)):
#         permute(s[:i] + s[i+1:], ans + s[i])

# s = input("Enter string: ")
# permute(s)

from itertools import permutations

s = input("Enter a string: ")

# generate permutations
perms = permutations(s)

print("Permutations:")
for p in perms:
    print("".join(p))