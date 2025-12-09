s = input("Enter String: ").lower()

l = 0
wrd = ""
newStr = ""
for i in range(len(s)):
    if s[i] != ' ':
        for j in range(i, len(s)):
            if s[j] == ' ':
                continue
            if s[j] not in newStr:
                newStr += s[j]
            else:
                if l < len(newStr):
                    wrd = newStr
                    l = len(newStr)
                    newStr = ""
                    print("Word:", wrd, "--> Length:", l)
                    break
                else:
                    newStr = ""
                    break