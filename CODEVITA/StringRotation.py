def rotate_string(s, direction, k):
    k = k % len(s)
    if direction == 'L':
        return s[k:] + s[:k]
    else:
        return s[-k:] + s[:-k]
    
def is_anagram_substring(original, target):
    n = len(target)
    sorted_target = sorted(target)

    for i in range(len(original) - n + 1):
        subStr = original[i:i+n]
        if sorted(subStr) == sorted_target:
            return True
        
        return False
    
def solve():
    s = input().strip()
    q = int(input().strip())
    
    original = s
    firstChars = ""
    
    for _ in range(q):
        d, r = input().split()
        r = int(r)
        s = rotate_string(s, d, r)
        first_chars += s[0]
        
    if is_anagram_substring(original, first_chars):
        print("YES")
    else:
        print("NO")

solve()