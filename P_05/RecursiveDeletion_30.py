def empty(s, p):
    if s == "": return True
    if p not in s: return False
    i = s.find(p)
    while i != -1:
        if empty(s[:i] + s[i+len(p):], p):
            return True
        i = s.find(p, i+1)
    return False

s = input("Enter string: ")
p = input("Enter substring: ")

print("Can become empty" if empty(s, p) else "Cannot become empty")
