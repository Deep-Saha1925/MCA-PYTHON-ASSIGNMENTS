lst = ["apple", "banana", "grape", "kiwi"]
k = int(input("Enter K: "))

def freq(word):
    if k < len(word):
        ch = word[k]
        return word.count(ch)
    return 0

lst.sort(key=freq)

print(lst)