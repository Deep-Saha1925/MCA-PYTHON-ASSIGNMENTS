# 1 fix: TODO
# s = input("Enter String: ")
# l = []
# for ch in s:
#     l.append(0)

# newStr = ""
# for i in range(len(s)):
#     if s[i] not in newStr:
#         newStr += s[i]+str(i+1)
#     else:
#         idx = newStr.find(s[i]) + 1
#         l[i] = int(newStr[idx])
#         newStr = newStr[:idx] + str(i+1) + newStr[idx+1:]
# print(l)

# s = input("Enter String: ")
s = "abbccbb"
l = []
for ch in s:
    l.append(0)

for i in range(len(s)):
    for x in range(i-1, -1, -1):
        if s[x] == s[i]:
            l[i] = x+1
            break
                
print(l)